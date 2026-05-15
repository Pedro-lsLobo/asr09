import zmq
import sys

def main():
    publisher_host = sys.argv[1] if len(sys.argv) > 1 else "localhost"
    port           = sys.argv[2] if len(sys.argv) > 2 else "12345"
    count          = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    address        = "tcp://" + publisher_host + ":" + port

    context = zmq.Context()
    socket  = context.socket(zmq.SUB)           # create subscriber socket
    socket.connect(address)                     # connect to remote publisher
    socket.setsockopt(zmq.SUBSCRIBE, b"TIME")   # subscribe to TIME messages
    print("Subscribed to " + address + ". Waiting for " + str(count) + " messages...")

    for i in range(count):
        msg = socket.recv()                     # receive a matching message
        print(msg.decode())                     # print the result

    print("Done.")

if __name__ == "__main__":
    main()
