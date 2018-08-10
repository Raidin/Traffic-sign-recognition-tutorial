TOOLS=$HOME/caffe-for-imagenet/build/tools
#rm -rf log/lenet/*
$TOOLS/caffe train --solver=./lenet/lenet_solver.prototxt --gpu 0,1,2,3,4,5,6,7 -log_dir="./log/lenet"
