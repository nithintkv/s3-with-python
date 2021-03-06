import boto.s3
import sys
from boto.s3.key import Key

AWS_ACCESS_KEY_ID = 'ACCESS_KEY'
AWS_SECRET_ACCESS_KEY = 'SECRET_KEY'

bucket_name = 'bucket_name'
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)


bucket = conn.create_bucket(bucket_name,
    location=boto.s3.connection.Location.DEFAULT)

testfile = "demo_file.pdf"
print('Uploading %s to Amazon S3 bucket %s')


def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()


k = Key(bucket)
k.key = 'my test file'
k.set_contents_from_filename(testfile,
    cb=percent_cb, num_cb=10)