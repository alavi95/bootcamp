import os
import sys
sys.path.append(os.path.realpath(__file__).split("bootcamp")[0]+"bootcamp")

from lib.helper import *
import boto3



def upload_to_s3(bucket_name, path_to_file, file_name, content_type="", make_public=False):
    s3_client = boto3.client("s3", aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
    ExtraArgs = {}
    if content_type != "":
        ExtraArgs["ContentType"] = content_type
    pass
    if make_public:
        ExtraArgs["ACL" : "public-read"]
    pass
    if len(ExtraArgs) > 0:
        s3_client.upload_file(path_to_file, bucket_name, file_name, ExtraArgs=ExtraArgs)
    else:
        s3_client.upload_file(path_to_file, bucket_name, file_name)


def read_from_s3(bucket_name, file_name, to_path):
    if not to_path.endswith("/"):
        to_path += "/"
    to_path += file_name
    s3_client = boto3.client("s3", aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
    s3_client.download_file(bucket_name, file_name, to_path)
    return


def get_s3_contents(bucket_name):
    s3_resource = boto3.resource("s3", aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
    bucket = s3_resource.Bucket(bucket_name)
    files = []
    for file in bucket.objects.filter():
        files.append(file.key)
    return files