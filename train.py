import os
import argparse
import stat
import subprocess
from cfg import *
from easydict import EasyDict as edict

def train(val):
    run_soon = val.run_soon
    network = val.network_model

    job_dir = os.path.join(os.getcwd(), 'models', network)
    snapshot = os.path.join(job_dir, 'snapshot')
    solver_file = os.path.join(job_dir, '{}_solver.prototxt'.format(network))

    if not os.path.exists(snapshot):
        os.makedirs(snapshot)

    job_file = os.path.join(snapshot, 'train.sh')

    with open(job_file, 'w') as f:
        f.write('TOOLS={}/build/tools\n'.format(config.caffe_root))
        f.write('$TOOLS/caffe train \\\n')
        f.write('--solver="{}" \\\n'.format(solver_file))
        f.write('--gpu {} 2>&1 | tee {}/{}_train.log\n'.format(val.gpus, snapshot, network))

    # Run the job.
    os.chmod(job_file, stat.S_IRWXU)
    if run_soon:
      subprocess.call(job_file, shell=True)

    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("caffe_root", help="Please Input CAFFE HOME PATH(eg. /home/user/caffe)")
    parser.add_argument('--gpus', default='0', help='Define GPU device ID')
    parser.add_argument('--run-soon', default=False, action = "store_true", help='Directly Train Script Excuting')
    parser.add_argument('--network-model-name', default='lenet', help='Choose Applying Network Type(ex, lenet, resnet20, resnet32 etc)')

    args = parser.parse_args()

    tmp_cfg = edict()
    tmp_cfg.caffe_root = args.caffe_root
    tmp_cfg.gpus = args.gpus
    tmp_cfg.network_model = args.network_model_name
    tmp_cfg.run_soon = args.run_soon
    update_config(tmp_cfg)

    train(val=tmp_cfg)