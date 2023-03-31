#!/bin/sh -e

docker build . -t registry1.ctdn.net/library/ai-generator-web-api:latest

docker push registry1.ctdn.net/library/ai-generator-web-api:latest
