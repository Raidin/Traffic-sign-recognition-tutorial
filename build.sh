CAFFE_HOME=$1

if [ -z "$1" ]
	then
	echo "No argument supplied, Please Input CAFFE HOME PATH(eg. /home/user/caffe)"
	exit
fi

echo " - Input CAFFE_HOME DIR ::" $CAFFE_HOME

cd $CAFFE_HOME

echo " - CAFFE BUILD START.........."
make all -j$(nproc)
echo " - CAFFE BUILD COMPLETED.........."
