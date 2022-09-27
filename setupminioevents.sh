sudo apt-get -y update

curl https://dl.min.io/client/mc/release/linux-amd64/mc \
  --create-dirs \
  -o $HOME/minio-binaries/mc

chmod +x $HOME/minio-binaries/mc
export PATH=$PATH:$HOME/minio-binaries/

cd $HOME/minio-binaries

./mc alias set MINIO "http://$1:$2" minioadmin minioadmin

./mc admin config set MINIO notify_webhook endpoint="http://$1:$2/hooks/redeploy-webhook"


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
    MINIO/$3 \
    arn:minio:sqs::_:webhook
    