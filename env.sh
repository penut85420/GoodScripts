#!/bin/bash
docker run -it --rm \
    -u $(id -u):$(id -g) \
    --gpus all \
    -v "$PWD":/home \
    -e "TZ=Asia/Taipei" \
    tensorflow:v2 /bin/bash
