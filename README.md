# cryptoapi

## Description

This is a small project to demonstrate an automation pipeline in Github Action. The program is a rest api service that queries spot price for Bitcoin in multiple currencies available on Coinbase. The pipeline is triggered whenever there's a push or pull request made to the repo.

## The pipeline

The pipeline consists of three different stages:

1. Build the docker image of the api and push to the Dockerhub repo as `:test` image. `:test` is chosen for simplicity, it can be tagged with the commit message to make sure developers won't accidentally overwrite each other's test images. Unittest can be done at this stage if we'd like to.

2. Spin up the api and run tests against it, if the test fails, it won't move on to the next stage. Hence, the production image won't change

3. If the previous step passes, deploy the docker image to `:latest` version and send a slack notification.

After the third stage, the deployment to production depends on how the current pipeline is structured.