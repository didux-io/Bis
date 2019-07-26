#!/bin/sh

# Login to AWS repositories
$(aws ecr get-login --no-include-email --region eu-central-1)

# Build production container
docker build --no-cache -t didux/tis:prod .
docker tag didux/tis:prod 462619610638.dkr.ecr.eu-central-1.amazonaws.com/didux/tis:prod
docker push 462619610638.dkr.ecr.eu-central-1.amazonaws.com/didux/tis:prod

# Build arm container
docker build --no-cache -t  didux/tis:arm -f Dockerfile-arm .
docker tag didux/tis:arm 462619610638.dkr.ecr.eu-central-1.amazonaws.com/didux/tis:arm
docker push 462619610638.dkr.ecr.eu-central-1.amazonaws.com/didux/tis:arm

# upload to dockerhub
docker tag didux/tis:arm diduxio/tis:arm
docker tag didux/tis:prod diduxio/tis:latest
docker push diduxio/tis:arm
docker push diduxio/tis:latest