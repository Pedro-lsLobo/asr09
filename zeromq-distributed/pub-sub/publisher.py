import zmq
import time
import sys

def main():
    port = sys.argv[1] if len(sys.argv) > 1 else "12345"

    context = zmq.Context()
    socket  = context.socket(zmq.PUB)       # create publisher socket
    socket.bind("tcp://*:" + port)          # bind to all interfaces
    print("Publisher bound to port " + port + ". Publishing every 5 seconds...")

    while True:
        time.sleep(5)                       # wait 5 seconds between publishes
        t = "TIME " + time.asctime()
        socket.send(t.encode())             # publish current time
        print("Published: " + t)

if __name__ == "__main__":
    main()
