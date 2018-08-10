import os
import time

data_root= '{}/data'.format(os.environ['HOME'])
if not os.path.exists(data_root):
	os.makedirs(data_root)

def download_data(file_name):
	dataset_home = 'http://benchmark.ini.rub.de/Dataset'
	store_path = os.path.join(data_root, file_name)
	download_url = '%s/%s'%(dataset_home, file_name)
	if not os.path.isfile(store_path):
		print 'Download [ {} ] ...'.format(file_name)
		os.system('wget -O {} {}'.format(store_path, download_url))

def unzip_file(file_name, option=''):
	file_path = os.path.join(data_root, file_name)
	if os.path.isfile(file_path):
		os.system('unzip -o {} {}'.format(file_path, option))
	else:
		print '[ {} ] is not exists...'.format(file_name)

def main():
	test_data_gt = 'GTSRB_Final_Test_GT.zip'
	test_data = 'GTSRB_Final_Test_Images.zip'
	training_data = 'GTSRB_Final_Training_Images.zip'

	# Download Dataset
	# Test Data GT
	download_data(test_data_gt)
	# Test Data
	download_data(test_data)
	# Training Data
	download_data(training_data)

	# Unzip Files
	if not os.path.isfile(os.path.join(data_root, 'GTSRB',test_data_gt)):
		unzip_file(test_data_gt, '-d {}/GTSRB'.format(data_root))
	if not os.path.isdir(os.path.join(data_root, 'GTSRB/Final_Test')):
		unzip_file(test_data, '-d {}'.format(data_root))
	if not os.path.isdir(os.path.join(data_root, 'GTSRB/Final_Training')):
		unzip_file(training_data, '-d {}'.format(data_root))

if __name__ == '__main__':
	main()
	print 'Completed GTSRB Dataset Download...'
	time.sleep(0.5)