#!/bin/sh

$(aws ecr get-login --no-include-email --region eu-west-1)

docker build --no-cache -t didux/bis:latest .
#docker build -t didux/bis:latest .
docker tag didux/bis:latest 462619610638.dkr.ecr.eu-west-1.amazonaws.com/didux/bis:latest
docker push 462619610638.dkr.ecr.eu-west-1.amazonaws.com/didux/bis:latest