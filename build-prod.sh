#!/bin/sh

# Login to AWS repositories
$(aws ecr get-login --no-include-email --region eu-central-1)

# Build production container
docker build --no-cache -t didux/bis:prod .
docker tag didux/bis:prod 462619610638.dkr.ecr.eu-central-1.amazonaws.com/didux/bis:prod
docker push 462619610638.dkr.ecr.eu-central-1.amazonaws.com/didux/bis:prod

# Build arm container
docker build --no-cache -t  didux/bis:arm -f Dockerfile-arm .
docker tag didux/bis:arm 462619610638.dkr.ecr.eu-central-1.amazonaws.com/didux/bis:arm
docker push 462619610638.dkr.ecr.eu-central-1.amazonaws.com/didux/bis:arm

# upload to dockerhub
docker tag didux/bis:arm diduxio/bis:arm
docker tag didux/bis:prod diduxio/bis:latest
docker push diduxio/bis:arm
docker push diduxio/bis:latest