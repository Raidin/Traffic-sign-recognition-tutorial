import os
import argparse
import stat
import subprocess
from cfg import *
from easydict import EasyDict as edict

def test(val):
    run_soon = val.run_soon
    network = val.network_model

    job_dir = os.path.join(os.getcwd(), 'models', network)
    snapshot = os.path.join(job_dir, 'snapshot')
    testnet_file = os.path.join(job_dir, '{}_testnet.prototxt'.format(network))

    # Find most snapshot.
    max_iter = 0
    for file in os.listdir(snapshot):
        if file.endswith(".caffemodel"):
            basename = os.path.splitext(file)[0]
            print basename
            iter = int(basename.split('_iter_')[1])
            if iter > max_iter:
                max_iter = iter

    weights_model = os.path.join(snapshot, "_iter_{}.caffemodel".format(max_iter))


    if not os.path.exists(snapshot):
        os.makedirs(snapshot)

    job_file = os.path.join(snapshot, 'test.sh')

    with open(job_file, 'w') as f:
        f.write('TOOLS={}/build/tools\n'.format(config.caffe_root))
        f.write('$TOOLS/caffe test \\\n')
        f.write('--model="{}" \\\n'.format(testnet_file))
        f.write('--weights="{}" \\\n'.format(weights_model))
        f.write('--iterations="{}" \\\n'.format(100))
        f.write('--gpu {} 2>&1 | tee {}/{}_test.log\n'.format(val.gpus, snapshot, network))

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

    test(val=tmp_cfg)