import os
from easydict import EasyDict as edict

config = edict()

config.caffe_root = 'path/to/caffe_root'

# create_lmdb global config
config.data_root = os.path.join(os.environ['HOME'],'data/GTSRB')
config.train_root = os.path.join(config.data_root, 'Final_Training/Images')
config.test_root = os.path.join(config.data_root, 'Final_Test/Images')

def update_config(config_file):
    print 'update_config...'
    for k, v in config_file.items():
        if k in config:
            config[k] = v
