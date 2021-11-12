# ZeroMQ Pipeline Example 

## Description

This is an example of a ZeroMQ based pipeline that streams around a bunch of arrays.

In more detail, it does the following.

1. `00_h5tomat.py` reads an HDF5 file, loops the frames, and dumps two matrices into a Matlab `.mat` formatted file.
2. `01_source_watchdog.py` watches the specified directory for these `.mat` files to show up. More specifically, it watches the directory for them to be renamed. (To avoid race and lock conditions, files are originally written with a `.` prefix and then renamed to their final format.) The arrays `im` and `depth` are read from the `.mat` file, converted to Numpy arrays, serialized, and then streaming through ZeroMQ.
3. `02_processor.py` accepts the arrays through a socket, does some processing (actually, it does nothing right now, but it could), and then streams the contents onwards.
4. `03_sink.py` is the final recipient of the arrays. By default, it will display the `im` matrix as a video using OpenCV.

If you don't have the HDF5 file with imaging data around, the script `genB.m` can generate random arrays with data. The script runs in Matlab and Octave, but you need to adjust the syntax of the `save` statement depending on whether you use Matlab or Octave.

## Prerequisites

```bash
$ conda create --name zmqdemo
$ conda activate zmqdemo
$ conda install scipy numpy
$ conda install zeromq watchdog
$ pip install opencv-python
```

## Contact & Blame

- Volker Hoffmann (volker.hoffmann@sintef.no)
