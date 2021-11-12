"""
Dump HDF5 File to Mat Files.

Call Signaure:
$ python ./genC.py --input /data/storage/
"""

import argparse
import scipy.io as sio
import h5py
import time
import os


# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input',
                    default='/data/seavention/Dev/Simple_Im1_Depth_NFrames100.h5',
                    help='HDF5 File.')
args = parser.parse_args()


# load hdf5
# dump frames as .mat
with h5py.File(args.input, 'r') as fx:
    im = fx['im1'][:]
    depth = fx['depth'][:]
    # dump successive frames as .mat
    for nframe in range(40):
        print(im[nframe,:,:].shape)
        fname_write = ".99_%08d_A.mat" % nframe
        fname_done = "99_%08d_A.mat" % nframe
        sio.savemat(fname_write, mdict={'depth': depth[nframe,:,:],
                                  'im': im[nframe,:,:]},
                    format='5')
        os.rename(fname_write, fname_done)
        time.sleep(0.1)
    
