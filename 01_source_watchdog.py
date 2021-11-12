import zmq
import pickle
import numpy as np
import time
import scipy.io as sio
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class EventToSocket(FileSystemEventHandler):
    def __init__(self, socket):
        super().__init__()
        self.socket = socket

    def on_moved(self, event):
        if event.dest_path[-3:] == 'mat':
            mat = sio.loadmat(event.dest_path)
            im = mat['im']
            depth = mat['depth']
            print(im)
            print(depth)
            self.socket.send_multipart([b'utofia',
                                        pickle.dumps(im),
                                        pickle.dumps(depth)])


def main():
    # Setup Communications
    context_out = zmq.Context()
    socket_out = context_out.socket(zmq.PUB)
    socket_out.bind("tcp://*:5556")

    # Setup Watchdog
    my_event_handler = EventToSocket(socket=socket_out)
    my_observer = Observer()
    my_observer.schedule(my_event_handler, '.', recursive=False)
    my_observer.start()

    # Loop Watchdog
    try:
        while True:
            time.sleep(0.1)
    finally:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    main()
