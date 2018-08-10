#!/usr/bin/env sh

TOOLS=$HOME/caffe-for-imagenet/build/tools

$TOOLS/caffe test \
    --model=./lenet/lenet_train_test.prototxt \
    --weights=./lenet/snapshot/1_GPU/_iter_20000.caffemodel \
    --gpu 0 \
     --iterations=100 \
    -log_dir="./log"

