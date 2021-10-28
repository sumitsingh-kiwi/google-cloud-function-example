#!/bin/bash

TIME=`date +%b-%d-%y`
FILENAME=Leasera-service-backup-$TIME
tar -czvf $FILENAME.tar.gz .
gsutil cp $FILENAME.tar.gz gs://build-code-backup/

gcloud run deploy helloworld --source=hello_world --region=us-central1 --allow-unauthenticated


