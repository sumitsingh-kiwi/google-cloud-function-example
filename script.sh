#!/bin/bash

gcloud functions deploy leasera --region=us-central1 --source=google-function-example --trigger-http --runtime=python37
