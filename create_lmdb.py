import argparse
import os
import subprocess
import stat
from cfg import *
from easydict import EasyDict as edict

def check_before_lmdb(path):
    if os.path.exists(path):
        filenames = os.listdir(path)
        for filename in filenames:
            full_filename = os.path.join(path, filename)
            os.remove(full_filename)
        os.rmdir(path)

def create_lmdb(data, label, data_type):
    store_dir = os.path.join(lmdb_store_path, data_type)
    link_dir = os.path.join(lmdb_link_path, data_type)

    check_before_lmdb(store_dir)

    cmd = "{}/build/tools/convert_imageset" \
        " --resize_height={}" \
        " --resize_width={}" \
        " --shuffle" \
        " --encoded={}" \
        " --encode_type={}" \
        " {} {} {}" \
        .format(config.caffe_root, 32, 32, True, 'png', data, label, store_dir)

    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]

    if os.path.exists(link_dir):
        os.unlink(link_dir)
    os.symlink(store_dir, link_dir)

    return link_dir

def create_mean_binary():
    store_dir = os.path.join(lmdb_store_path, 'train_mean.binaryproto')
    link_dir = os.path.join(lmdb_link_path, 'train_mean.binaryproto')

    lmdb = os.path.join(config.data_root, 'lmdb/train_lmdb')
    if not os.path.isdir(lmdb):
        print 'Please creating train lmdb...'

    create_mean_binary_job_file = './create_mean_binary_job_file.sh'

    with open(create_mean_binary_job_file, 'w') as f:
        f.write('TOOLS={} \n'.format('{}/build/tools'.format(config.caffe_root)))
        f.write('GLOG_logtostderr=1  $TOOLS/compute_image_mean \\\n')
        f.write('{} \\\n'.format(lmdb))
        f.write('{} '.format(store_dir))

    os.chmod(create_mean_binary_job_file, stat.S_IRWXU)
    subprocess.call(create_mean_binary_job_file, shell=True)

    os.remove(create_mean_binary_job_file)

    if os.path.exists(link_dir):
        os.unlink(link_dir)
    os.symlink(store_dir, link_dir)

def main():
    train_label = os.path.join(os.getcwd(), 'label/train_label.txt')
    test_label = os.path.join(os.getcwd(), 'label/test_label.txt')

    # Create Test Data LMDB
    test_lmdb = create_lmdb(config.test_root, test_label, 'test_lmdb')
    train_lmdb = create_lmdb(config.train_root, train_label, 'train_lmdb')

    # Create Mean Binary
    create_mean_binary()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("caffe_root", help="Please Input CAFFE HOME PATH(eg. /home/user/caffe)")

    args = parser.parse_args()

    tmp_cfg = edict()
    tmp_cfg.caffe_root = args.caffe_root
    update_config(tmp_cfg)

    lmdb_store_path = os.path.join(config.data_root, 'lmdb')
    if not os.path.exists(lmdb_store_path):
        os.makedirs(lmdb_store_path)

    lmdb_link_path = os.path.join(os.getcwd(), 'lmdb')
    if not os.path.exists(lmdb_link_path):
        os.makedirs(lmdb_link_path)

    main()