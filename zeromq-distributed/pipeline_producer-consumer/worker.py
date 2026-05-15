import zmq
import time
import pickle
import sys

def main():
    worker_id     = sys.argv[1] if len(sys.argv) > 1 else "1"
    producer_host = sys.argv[2] if len(sys.argv) > 2 else "localhost"
    port          = sys.argv[3] if len(sys.argv) > 3 else "12345"
    address       = "tcp://" + producer_host + ":" + port

    context = zmq.Context()
    socket  = context.socket(zmq.PULL)      # create pull socket
    socket.connect(address)                 # connect to remote producer
    print("Worker " + worker_id + " connected to " + address)

    while True:
        print("Worker " + worker_id + " wants work")
        work = pickle.loads(socket.recv())  # receive work item from producer
        print("Worker " + worker_id + " gets   " + format(work, "03d"))
        time.sleep(work)                    # simulate processing time

if __name__ == "__main__":
    main()
