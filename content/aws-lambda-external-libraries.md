Title: How to Run External Python Libraries in AWS Cloud
Date: 2020-08-17 14:40
Category: Tools
Tags: AWS, cloud, lambda, biopython, wheels, Docker, packages, deployment, Klayers, pandas, SAAS, PYPI
Slug: aws-lambda-external-libraries
Authors: Bob
Summary: AWS Lambda is awesome, but sometimes it can be hard to get external libraries working in this serverless environment. No worries, we learned a lesson or two which I will share in this article. Ready to run almost any Python library in the cloud? This should excite you and even trigger your entrepeneurial mind ...
cover: images/featured/pb-article.png

AWS Lambda is awesome, but sometimes it can be hard to get external libraries working in this serverless environment.

No worries, we learned a lesson or two which I will share in this article.

Ready to run almost any Python library in the cloud? This should excite you and even trigger some of you to think about building your own SAAS ...

## What is AWS Lambda? First steps

> Amazon Web Services (AWS) Lambda is an on-demand compute service that lets you run code in response to events or HTTP requests ([source](https://realpython.com/code-evaluation-with-aws-lambda-and-api-gateway/))

If you are new to this technology, I recommend rolling your own lambda using only Python's standard library (simplest use case):

1. Follow [this article](https://realpython.com/code-evaluation-with-aws-lambda-and-api-gateway/) to set up a Lambda function and configuring an AWS Gateway API endpoint to invoke the lambda.

2. Make an AWS account and take [our code challenge #36](https://codechalleng.es/challenges/36/) and/or play with [our example repo](https://github.com/bbelderbos/first-aws-lambda).

For inspiration, here is how we use AWS Lambda on [our coding platform](https://codechalleng.es/):

![PyBites platform aws lambda use]({filename}/images/pybites-platform-architecture.png)

## Use external libraries

Now that you have an AWS lambda running, the next challenge is how to work with [external dependencies](https://pypi.org/).

Lambda is a sandbox with Python's standard library, any external packages you need to install yourself, typically using a virtual environment and creating a zipfile of lambda function code + dependencies (see [the docs](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html)).

The procedure is something like this after you've created your virtual env and pip installed the packages you want to use:

	(venv) $ cd venv/lib/python3.8/site-packages/
	(venv) $ zip -r9 lambda.pkg.zip *
	(venv) $ ls -lrth *zip  # should be < 50 MB (use Klayers to reduce size - see next)
	(venv) $ mv lambda.pkg.zip ../../../../
	(venv) $ cd ../../../../
	(venv) $ zip -g lambda.pkg.zip lambda.py

Basically we put the lambda script ([example code](https://github.com/bbelderbos/first-aws-lambda/blob/master/pep_lambda.py)) and all the pip installed package at the same top level directory and recursively zip it up. This zip file you would upload in your lambda's _Function code_ section:

![Upload lambda zip file]({filename}/images/deploy-lambda-zip.png)

## Add AWS Lambda Layers

This does not work for all packages though. When we introduced [`pandas` Bites](https://codechalleng.es/bites/search/pandas), we could not just take the package we pip installed on our Mac and expect it to work in a Linux environment. We needed a Linux compatible package.

Thankfully [AJ](pages/guests.html#ajkerrigan) tipped us about [Keith's Layers (Klayers)](https://github.com/keithrozario/Klayers) which gives compiled packages you can add using the [AWS Lambda layers feature](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).

You can just select the [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) for [your region](https://github.com/keithrozario/Klayers/tree/master/deployments/python3.8/arns) and add it to your Lambda's layers. For example:

![Lambda Layers example]({filename}/images/klayers-example.png)

## Add pre- or self-compiled packages

_Klayers_ only offer a subset of packages though. Yesterday we had to get `biopython` working for [Bite 298](https://codechalleng.es/bites/298/) and there was not a _Klayer_ nor did the locally pip installed package work due to missing compiled files.

Luckily the Bite Author, [Chris](https://twitter.com/schustercf?lang=en), found an answer:

[How do I add Python packages with compiled binaries to my deployment package and make the package compatible with Lambda?](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-python-package-compatible/)

You can download the `.whl` (wheel) file and unzip that in your root lambda folder which then gives you the OS compatible files.

> A wheel is a ZIP-format archive with a specially formatted file name and the .whl extension ([source](https://www.python.org/dev/peps/pep-0427/))

In this case we just had to use the `manylinux1` version for our lambda:

	(venv) $ unzip -l biopython-1.77-cp38-cp38-manylinux1_x86_64.whl | head
	Archive:  biopython-1.77-cp38-cp38-manylinux1_x86_64.whl
	Length      Date    Time    Name
	---------  ---------- -----   ----
		3267  05-24-2020 23:07   biopython-1.77.dist-info/LICENSE.rst
		108  05-24-2020 23:07   biopython-1.77.dist-info/WHEEL
		11  05-24-2020 23:07   biopython-1.77.dist-info/top_level.txt
		3267  05-24-2020 23:07   biopython-1.77.dist-info/LICENSE
		12659  05-24-2020 23:07   biopython-1.77.dist-info/METADATA
		53906  05-24-2020 23:07   biopython-1.77.dist-info/RECORD
		...
		...

(Note that `biopython` has `numpy` as dependency, but we already added that via a _Klayer_.)

And now we have `biopython` running on our platform, awesome!

If for some reason the package on PYPI does not have compatible _wheels_, as a last resource you can try to use [docker-lambda](https://github.com/lambci/docker-lambda) to compile your own.

> You can use docker-lambda for running your functions in the same strict Lambda environment, knowing that they'll exhibit the same behavior when deployed live. You can also use it to compile native dependencies knowing that you're linking to the same library versions that exist on AWS Lambda and then deploy using the AWS CLI. [README]

### How we managed to setup a scikit-learn AWS Lambda Layer

In this section we want to dive a little deeper into the topic of how to setup your own AWS Lambda Layer with any Python package. In particular, we wanted to support the well-known machine learning library [scikit-learn](https://scikit-learn.org/stable/). Once you understood the main steps, you are able to setup your own layers in no time.

In general, the idea is to mirror the Lambda environment, install dependencies with `pip` like in any other Python project, and ship these dependencies as Lambda layer. Easy, isn't it?

As mentioned above, for mirroring the Lambda environment, we use [docker-lambda](https://github.com/lambci/docker-lambda).

First, we create a new folder, for example `scikit-learn-layer`, and create a `requirements.txt` in which we put all the dependencies that we want later to be part of the Lambda layer. In our case, this is `scikit-learn`, so this is the only line in our `requirements.txt` file. 
Of course, you can add a specific version or a condition. 

Next, we run docker and mount our current working directory:

```BASH
$ docker run --rm -v $(pwd):/foo -w /foo lambci/lambda:build-python3.8 \
	pip install -r requirements.txt -t python
```

Assuming, you already have a working [docker](https://www.docker.com/) installation, we start with
calling `docker run`, targeting the `lambci/lambda` image, which offers various Python builds. For our platform, we use Python 3.8, but there is support for all major Python versions, so you can easily change the version to your needs. After docker has pulled the image, it will run the command `pip install -r requirements.txt -t python`, which will install all dependencies listed in the file `requirements.txt` to the target directory specified by `-t` option. While this is happening inside the container, because the container works in a directory that is mounted, the output will also be available in the host system.

When the docker process has finished, you should have the scikit-learn package along with all dependencies within the newly created python folder.

Next, we zip this folder: `zip -r scikit-learn.zip python`.

Now things get interesting. The next step would be to create or _publish_ a new AWS Lambda layer
based on our zipped dependencies. The easiest way to do this is to use the [AWS CLI](https://aws.amazon.com/de/cli/) tool, so go over there and grab your version. 

When you have installed the AWS cli tool, run `aws configure` once to set your credentials and your default region. You find your credentials under _My Security Credentials_ -> _Access Keys_. You may need to create a new Access Key.

We need to use the [publish-layer-version](https://docs.aws.amazon.com/cli/latest/reference/lambda/publish-layer-version.html) command. This commands supports the creation of Lambda layers either from zip files or from S3 buckets. In general, S3 is favored over zip files and will be faster, especially for larger files. 

Therefore, we head over to our [AWS Management Console](https://aws.amazon.com/console/) and create a new S3 bucket for our Lambda layer. 

> Most AWS services are region based and this holds true for Lambda functions, Lambda layers and S3 buckets. This means, you have to deploy these services in the same region, otherwise they cannot see each other!

With our newly available S3 bucket in the right region, we can finally copy our zip file over to S3 with the [s3 cp](https://docs.aws.amazon.com/cli/latest/reference/s3/) command. 

```BASH
$ aws s3 cp scikit-learn.zip s3://<your-bucket-name> --region <your-target-region>
```

Once the process has finished, you can see your zip file in the S3 bucket. Time to create our Lambda layer!

```BASH
$ aws lambda publish-layer-version \
	--layer-name scikit-learn \
    --description "Scikit-learn for Python 3.8" \
    --compatible-runtimes python3.7 python3.8 \
    --content S3Bucket=<your-bucket-name>,S3Key=scikit-learn.zip
```

As you can see, the command is straight forward and all information are available at this point.
If the command is successful, you are rewarded with a JSON response informing you about the layer's `arn`, which can be used in Lambda functions to connect the function to a Lambda layer.

And that's it! You have successfully created your first Lambda layer with a Python package that you can now use to import this package in your Lambda function. You can do this via the web interface, or again, via the AWS cli's [update-function-configuration](https://docs.aws.amazon.com/cli/latest/reference/lambda/update-function-configuration.html) command:

```BASH
$ aws lambda update-function-configuration \
    --function-name <your-lambda-function> \
    --layers <layer-arn:version-number> <layer-arn:version-number> <...>
```

This command again rewards you with a JSON response, which should have the key-value pair "LastUpdateStatus": "Successful".

To test your scikit-learn dependency, you should now be able to call

```PYTHON
import sklearn
print(sklearn.__version__)
```

within your Lambda function.

Finally, if you want to share your layer with others, you have to grant the right permissions via the [add-layer-version-permission](https://docs.aws.amazon.com/cli/latest/reference/lambda/add-layer-version-permission.html) command. You can grant access for certain roles and users, or allow public access like in the following example:

```BASH
aws lambda add-layer-version-permission \
    --layer-name scikit-learn \
    --principal "*" \
    --action lambda:GetLayerVersion \
    --version-number <your-layer-version> \
    --statement-id public \
    --region <your-target-region>
```

This concludes this section. Of course there is always more to learn, so if you want to go further and beyond this manual process, look into [AWS SAM](https://aws.amazon.com/blogs/compute/working-with-aws-lambda-and-lambda-layers-in-aws-sam/).

---

I hope this was useful and inspired you to get your own lambda working with your own favorite external library.

You'll soon notice the possibilities are endless and you can do this for fun and profit (more below).

Keep Calm and Code in Python!

-- Bob

---

Do you like what you've read so far? Do you have **an idea** you think you can develop into a **SAAS product** over time?

We can help you turn your cool idea into a **business**. We have turned our Python knowledge into products, leveraging **serverless** technology like AWS Lambda along the way.

And now we help our clients do the same.

Let us help you design your app and guide you while you implement it. Talking is easy, even _Python exercising_ can only push you that far. Coding (and designing) a **complete product** end-to-end is much harder.

Ready to build your **dream app**? [Book a **strategy session** with us](https://pybit.es/pages/apply.html). We want to help you.

Remember, the best time to plant a tree is yesterday.
