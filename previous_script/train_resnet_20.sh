TOOLS=$HOME/caffe-for-imagenet/build/tools
rm -rf ./log/resnet_20/*
$TOOLS/caffe train --solver=./resNet/resnet_20_solver_for_GTSRB.prototxt --gpu 0  -log_dir="./log/resnet_20"
