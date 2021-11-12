import sys
import zmq
import pickle


# Inbound 
context_in = zmq.Context()
socket_in = context_in.socket(zmq.SUB)
socket_in.connect("tcp://localhost:5556")

# Outbound
context_out = zmq.Context()
socket_out = context_out.socket(zmq.PUB)
socket_out.bind("tcp://*:6667")

# Subscribe
socket_in.setsockopt_string(zmq.SUBSCRIBE, 'utofia')

# Process and Pass Onwards
while True:
    # receive
    [topic,msg_im,msg_depth] = socket_in.recv_multipart()
    im = pickle.loads(msg_im)
    depth = pickle.loads(msg_depth)

    # print
    print(im)
    print(depth)

    # make this something OpenCV likes?

    # send
    socket_out.send_multipart([b'utofia_processed',
                               pickle.dumps(im),
                               pickle.dumps(depth)])
   