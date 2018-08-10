echo "Mean Binaryproto Creating Initialize......"
CAFFE_NAME=caffe-for-imagenet
WORKING_DIRECTORY=jihun_work
TOOLS=$HOME/$CAFFE_NAME/build/tools
DATA=$HOME/$CAFFE_NAME/$WORKING_DIRECTORY/traffic_sign_classification/GTSRB_lmdb

sleep 1
echo "Create mean Binaryproto....."
sleep 1

GLOG_logtostderr=1 $TOOLS/compute_image_mean $DATA/GTSRB_train_lmdb $DATA/train_mean.binaryproto
sleep 1
echo "Completed train dataset converting to mean binaryproto."

GLOG_logtostderr=1 $TOOLS/compute_image_mean $DATA/GTSRB_test_lmdb $DATA/test_mean.binaryproto
sleep 1
echo "Completed test dataset converting to binaryproto."

sleep 1
echo "Done..."
