import boto3

AWS_S3_ACCESS_KEY_ID = 'ACCESS_KEY'
AWS_S3_SECRET_ACCESS_KEY = 'SECRET_KEY'
AWS_STORAGE_BUCKET_NAME = 'BUCKET_NAME'

session = boto3.Session(
        aws_access_key_id=AWS_S3_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_S3_SECRET_ACCESS_KEY
    )
s3 = session.resource('s3')

s3.Object(AWS_STORAGE_BUCKET_NAME, 'new_name').copy_from(CopySource=AWS_STORAGE_BUCKET_NAME+'/oldname')
s3.Object(AWS_STORAGE_BUCKET_NAME, 'oldname').delete()