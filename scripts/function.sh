#!/bin/bash

TIME=`date +%b-%d-%y`
FILENAME=Leasera-functions-backup-$TIME
tar -czvf $FILENAME.tar.gz .
gsutil cp $FILENAME.tar.gz gs://build-code-backup/

gcloud functions deploy leasera --region=us-central1 --source=google-function-example --trigger-http --runtime=python37

#gcloud functions deploy publish --region=us-central1 --source=google-pub-sub-example --trigger-http --runtime=python37

#gcloud functions deploy subscribe --region=us-central1 --source=google-pub-sub-example --trigger-topic queueDemo --runtime=python37
