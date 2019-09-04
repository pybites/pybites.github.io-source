Title: How to Cleanup S3 Objects and Unittest it
Date: 2019-09-02 21:00
Category: Testing
Tags: AWS, S3, freezegun, moto, boto3, testing, APIs, paginator, mock
Slug: guest-cleanup-s3-objects
Authors: Giuseppe Cunsolo
Summary: In this guest post Giuseppe shares what he learned having to cleanup a large number of objects in an S3 bucket. He introduces us to some `boto3` as well as `moto` and `freezegun` he used to test his code. Enter Giuseppe ...
cover: images/featured/pb-guest.png

In this guest post Giuseppe shares what he learned having to cleanup a large number of objects in an S3 bucket. He introduces us to some `boto3` as well as `moto` and `freezegun` he used to test his code. Enter Giuseppe ...

## Delete S3 objects

This is a bit of code I wrote for a much bigger script used to monitor and cleanup objects inside an S3 bucket. The rest of the script is proprietary and unfortunately cannot be shared.

The [script.py](https://github.com/markgreene74/python-projects/blob/master/delete-s3-objects/script.py) module contains the `cleanup()` function. It uses `boto3` to connect to AWS, pull a list of all the objects contained in a specific bucket and then delete all the ones older than `n` days.  

I have included a few examples of creating a `boto3.client` which is what the function is expecting as the first argument. The other arguments are used to build the path to the _directory_ inside the S3 bucket where the files are located. This path in AWS terms is called a _[Prefix](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/using-folders.html)_.

As the number of the objects in the bucket can be larger than 1000, which is the [limit for a single GET](https://docs.aws.amazon.com/AmazonS3/latest/API/v2-RESTBucketGET.html) in the `GET Bucket (List Objects) v2`, I used a [paginator](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/paginators.html) to pull the entire list. The objects removal follow the same principle and process batches of 1000 objects.

## Testing the code

Now this was all good and fun but the really **interesting** part was how to unittest this code, see [test_script.py](https://github.com/markgreene74/python-projects/blob/master/delete-s3-objects/test_script.py).

After some researching I found **[moto](https://pypi.org/project/moto/)**, the _Mock AWS Services_ library. It's brilliant! Using this library the test will _mock_ access to the S3 bucket and create several objects in the bucket. You can leave the dummy AWS credentials in the script as they won't be needed.

At this point I wanted to create multiple objects in the S3 mocked environment with different timestamps, but unfortunately I discovered that this was not possible. Once an S3 object is created its creation date (metadata) cannot be easily altered, see [the object-metadata docs](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-metadata) for reference.

Enter another awesome library called **[freezegun](https://pypi.org/project/freezegun/0.1.11/)**. I ended up using `freeze_time` in my tests to mock the date/time and create S3 objects with different timestamps. This way we can safely experiment with the logic of `cleanup()`, that is leaving objects older than n days and deleting everything else within the _prefix_.

Here is the test script's output:

```
$ python test_script.py 
mock-root-prefix/mock-sub-prefix/test_object_01 2019-08-29 00:00:00+00:00
mock-root-prefix/mock-sub-prefix/test_object_02 2019-08-28 00:00:00+00:00
mock-root-prefix/mock-sub-prefix/test_object_03 2019-08-27 00:00:00+00:00
mock-root-prefix/mock-sub-prefix/test_object_04 2019-08-26 00:00:00+00:00
mock-root-prefix/mock-sub-prefix/test_object_05 2019-08-25 00:00:00+00:00
mock-root-prefix/mock-sub-prefix/test_object_06 2019-08-24 00:00:00+00:00
<class 'botocore.client.S3'>
Cleanup S3 backups
Working in the bucket:         my-mock-bucket
The prefix is:                 mock-root-prefix/mock-sub-prefix/
The threshold (n. days) is:    4
Total number of files in the bucket:     7
Number of files to be deleted:           3
Deleting the files from the bucket ...
Deleted:        3
Left to delete: 0
.
----------------------------------------------------------------------
Ran 1 test in 0.798s

OK
```

Again you can find the code for this project [here](https://github.com/markgreene74/python-projects/tree/master/delete-s3-objects).

---

Keep Calm and Code in Python!

-- [Giuseppe](pages/guests.html#giuseppecunsolo)
