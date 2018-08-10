#!/usr/bin/env sh

TOOLS=$HOME/caffe-for-imagenet/build/tools

$TOOLS/caffe test \
    --model=./resNet/resnet_20_testnet_for_GTSRB.prototxt \
    --weights=./resNet/snapshot/resnet_20/_iter_15000.caffemodel \
    --gpu 0 \
    --iterations=126 \
    -log_dir="./log/resnet_20"

