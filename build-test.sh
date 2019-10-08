#!/bin/sh

$(aws ecr get-login --no-include-email --region eu-central-1)

docker build --no-cache -t didux/bis:test .

docker tag didux/bis:test 462619610638.dkr.ecr.eu-central-1.amazonaws.com/didux/bis:test
docker push 462619610638.dkr.ecr.eu-central-1.amazonaws.com/didux/bis:test