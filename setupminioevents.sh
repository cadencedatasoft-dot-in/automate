sudo apt-get -y update

curl https://dl.min.io/client/mc/release/linux-amd64/mc \
  --create-dirs \
  -o $HOME/minio-binaries/mc

chmod +x $HOME/minio-binaries/mc
export PATH=$PATH:$HOME/minio-binaries/

cd $HOME/minio-binaries

./mc alias set MINIO "http://$1:$2" $3 $4
# ./mc alias set MINIO "http://nkloudstorapi.fatbrain.io:9000" user01 Pass1234!
./mc admin config set MINIO notify_webhook endpoint="http://$1:$2/hooks/redeploy-webhook"
# ./mc admin config set MINIO notify_webhook endpoint="http://34.192.88.74:29000/hooks/redeploy-webhook"

# ./mc admin config set MINIO notify_webhook \
# endpoint="http://54.202.108.158:9000/hooks/redeploy-webhook" \
#     auth_token=""  \
#     queue_dir=""   \
#     queue_limit="" \
#     comment="image found"\
#     client_key=""\
#     client_cert=""

./mc admin config set MINIO notify_webhook \
endpoint="http://$1:$2/hooks/redeploy-webhook" \
    auth_token=""  \
    queue_dir=""   \
    queue_limit="" \
    comment="image found"\
    client_key=""\
    client_cert=""

./mc event add \
    --event "put"  \
    --suffix "img" \
    MINIO/$5 \
    arn:minio:sqs::_:webhook
    
./mc event add \
    --event "put"  \
    --suffix "img" \
    MINIO/demo \
    arn:minio:sqs::_:webhook    