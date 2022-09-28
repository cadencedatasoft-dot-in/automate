
from minio import Minio
from minio.credentials.providers import Credentials

class S3:
  def __init__(self, host, port, secure:bool):
    self.client: Minio = None
    self.host = host
    self.port = port
    self.secure = secure

  def login(self, user:str, password:str, region:str="my-region"):
    hostport = self.host + ":" + self.port
    try:
      self.client = Minio(
        self.host + ":" + self.port,
        secure=self.secure,
        access_key=user,
        secret_key=password,
        region=region,
      )

      buckets = self.client.list_buckets()

      if buckets:
        return True

    except Exception as e:
      print(str(e))
      return False

  def download_s3obj(self, bucket, object):
    try:
      data = self.client.get_object(bucket, object)
      with open('file.img', 'wb') as file_data:
          for d in data.stream(32*1024):
              file_data.write(d)
      return True

    except Exception as e:
      print(str(e))
      return False
      