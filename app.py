# app.py
import sys
from flask import Flask, request
from src.s3 import S3
from urllib.parse import unquote
from src.sys import Sys

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def webhook():
  if request.method == 'POST':
    print("Data received from Webhook is: ", request.json)
    return "Webhook received!"

@app.route('/hooks/redeploy-webhook', methods=['POST'])
def redeploy_webhook():
  try:
    if request.method == 'POST':
      params = request.json
      bucket = params['Records']['s3']['bucket']['name']
      obj = unquote(params['Records']['s3']['object']['key'])
      s3 = S3()
      s3.login( app.config.get('miniouser'), app.config.get('miniopass') )
      s3.download_s3obj(bucket, obj)
      sy = Sys()
      sy.spinInstance()
      return "You instance is running now"
  except Exception as e:
    print(str(e))
    return str(e)

if __name__ == '__main__':
  app.config['apiport'] = sys.argv[1]
  app.config['miniohost'] = sys.argv[2]
  app.config['miniouser'] = sys.argv[3]
  app.config['miniopass'] = sys.argv[4]
  app.run(host='0.0.0.0', port=app.config.get('apiport'))
