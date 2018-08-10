import caffe
import lmdb
import numpy as np
import matplotlib.pyplot as plt
from caffe.proto import caffe_pb2
import cv2
import os

lmdb_file = os.path.join(os.getcwd(), 'lmdb/train_lmdb')

lmdb_env = lmdb.open(lmdb_file)
lmdb_txn = lmdb_env.begin()
lmdb_cursor = lmdb_txn.cursor()
datum = caffe_pb2.Datum()

for key, value in lmdb_cursor:
    datum.ParseFromString(value)
    print ("Data Encoded :: " + str(datum.encoded))
    label = datum.label

    if datum.encoded == True:
        arr = np.frombuffer(datum.data, dtype='uint8')
        img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
        width = img.shape[1]
        height = img.shape[0]

    else:
        data = caffe.io.datum_to_array(datum)
        img = data.astype(np.uint8)
        img = np.transpose(img, (2, 1, 0)) # original (dim, col, row)

    print 'Label ::', label
    cv2.imshow('image', img)
    key = cv2.waitKey(0)
    if key == 27: # esc key --> exit this program...
        exit()