echo "LMDB Creating Initialize......"
CAFFE_NAME=caffe-for-imagenet
WORKING_DIRECTORY=jihun_work

TOOLS=$HOME/$CAFFE_NAME/build/tools

TRAIN_DATA_ROOT=/media/jihunjung/CoCoPam/Ubuntu/dataset/GTSRB/train/GTSRB/Final_Training/Images
TEST_DATA_ROOT=/media/jihunjung/CoCoPam/Ubuntu/dataset/GTSRB/test
#TRAIN_DATA_ROOT=/home/jihunjung/dataset/GTSRB/train
#TEST_DATA_ROOT=/home/jihunjung/dataset/GTSRB/test

DATA=$HOME/$CAFFE_NAME/$WORKING_DIRECTORY/traffic_sign_classification/GTSRB_lmdb

TRAIN_LMDB=GTSRB_train_lmdb
TEST_LMDB=GTSRB_test_lmdb

TRAIN_LABLE_FILE=/media/jihunjung/CoCoPam/Ubuntu/dataset/GTSRB/train/GTSRB/Final_Training/Images/train_caffe.txt
TEST_LABLE_FILE=/media/jihunjung/CoCoPam/Ubuntu/dataset/GTSRB/test/test_caffe.txt
#TRAIN_LABLE_FILE=/home/jihunjung/dataset/GTSRB/train_caffe.txt
#TEST_LABLE_FILE=/home/jihunjung/dataset/GTSRB/test_caffe.txt

sleep 1
echo "Convert imageset to LMDB DB....."
sleep 1

sleep 1
if [ -d "$DATA/$TRAIN_LMDB" ]; then
	echo "GTSRB_train_lmdb is existed."
	rm -rf gcn/*
else
	echo "Creating" $TRAIN_LMDB
	GLOG_logtostderr=1 $TOOLS/convert_imageset \
			--resize_height=32 --resize_width=32 --shuffle --encoded=true --encode_type=png \
			$TRAIN_DATA_ROOT/ \
			$TRAIN_LABLE_FILE \
			$DATA/$TRAIN_LMDB
fi
sleep 1
echo "Completed train dataset converting to lmdb."

sleep 1
if [ -d "$DATA/$TEST_LMDB" ]; then
	echo "GTSRB_train_lmdb is existed."
else
	echo "Creating" $TEST_LMDB
	GLOG_logtostderr=1 $TOOLS/convert_imageset \
			--resize_height=32 --resize_width=32 --shuffle --encoded=true --encode_type=png \
			$TEST_DATA_ROOT/ \
			$TEST_LABLE_FILE \
			$DATA/$TEST_LMDB
fi
sleep 1
echo "Completed test dataset converting to lmdb."
sleep 1
echo "Done....."
