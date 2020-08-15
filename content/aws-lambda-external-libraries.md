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
