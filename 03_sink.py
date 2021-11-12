import sys
import zmq
import pickle
import cv2


# Inbound 
context_in = zmq.Context()
socket_in = context_in.socket(zmq.SUB)
socket_in.connect("tcp://localhost:6667")

# Subscribe
socket_in.setsockopt_string(zmq.SUBSCRIBE, 'utofia_processed')

# Receive
while True:
   # receive
    [topic,msg_im,msg_depth] = socket_in.recv_multipart()
    im = pickle.loads(msg_im)
    depth = pickle.loads(msg_depth)

    # print
    # print(im)
    # print(depth)

    # show frame
    cv2.imshow('frame', im)
    cv2.waitKey(1)
