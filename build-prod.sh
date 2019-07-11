#!/bin/sh

$(aws ecr get-login --no-include-email --region eu-central-1)

docker build --no-cache -t didux/bis:prod .
docker tag didux/bis:prod 462619610638.dkr.ecr.eu-central-1.amazonaws.com/didux/bis:prod
docker push 462619610638.dkr.ecr.eu-central-1.amazonaws.com/didux/bis:prod

docker build --no-cache -t  didux/bis:arm -f Dockerfile-arm .
docker tag didux/bis:arm 462619610638.dkr.ecr.eu-central-1.amazonaws.com/didux/bis:arm
docker push 462619610638.dkr.ecr.eu-central-1.amazonaws.com/didux/bis:arm

docker tag didux/bis:arm diduxio/bis:arm
docker tag didux/bis:prod diduxio/bis:latest
docker push diduxio/bis:arm
docker push diduxio/bis:latest