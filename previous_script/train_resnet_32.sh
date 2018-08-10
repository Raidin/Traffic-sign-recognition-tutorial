TOOLS=$HOME/caffe-for-imagenet/build/tools

$TOOLS/caffe train --solver=./resNet/resnet_32_solver_for_GTSRB.prototxt --gpu 0  -log_dir="./log/resnet_32"
