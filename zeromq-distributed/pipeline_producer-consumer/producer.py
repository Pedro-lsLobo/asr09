import zmq
import time
import pickle
import random
import sys

def main():
    port     = sys.argv[1] if len(sys.argv) > 1 else "12345"
    nworkers = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    context = zmq.Context()
    socket  = context.socket(zmq.PUSH)      # create push socket
    socket.bind("tcp://*:" + port)          # bind to all interfaces
    print("Producer bound to port " + port + " (assuming " + str(nworkers) + " workers).")

    while True:
        workload = random.randint(1, 100)   # generate a random workload
        print("Produced workload " + format(workload, "03d"))
        socket.send(pickle.dumps(workload)) # push workload to next available worker
        time.sleep(workload / nworkers)     # pace production relative to worker count

if __name__ == "__main__":
    main()
