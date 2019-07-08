#!/bin/sh

$(aws ecr get-login --no-include-email --region eu-central-1)

docker build --no-cache -t  didux/bis:arm -f Dockerfile-arm .
docker tag didux/bis:arm 462619610638.dkr.ecr.eu-central-1.amazonaws.com/didux/bis:arm
docker push 462619610638.dkr.ecr.eu-central-1.amazonaws.com/didux/bis:arm