from boto.s3.connection import S3Connection, Bucket, Key

AWS_S3_ACCESS_KEY_ID = 'ACCESS_KEY'
AWS_S3_SECRET_ACCESS_KEY = 'SECRET_KEY'
AWS_STORAGE_BUCKET_NAME = 'BUCKET_NAME'

conn = S3Connection(AWS_S3_ACCESS_KEY_ID, AWS_S3_SECRET_ACCESS_KEY)
b = Bucket(conn, AWS_STORAGE_BUCKET_NAME)
k = Key(b)
k.key = 'file_to_delete'
b.delete_key(k)
