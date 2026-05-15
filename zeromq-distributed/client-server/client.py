import zmq
import sys

def main():
    server_host = sys.argv[1] if len(sys.argv) > 1 else "localhost"
    port        = sys.argv[2] if len(sys.argv) > 2 else "12345"
    address     = "tcp://" + server_host + ":" + port

    context = zmq.Context()
    socket  = context.socket(zmq.REQ)       # create request socket
    socket.connect(address)                 # connect to remote server
    print("Connected to server at " + address)

    socket.send(b"Hello world")             # send request
    message = socket.recv()                 # block until response
    print("Reply: " + message.decode())     # print result

    socket.send(b"STOP")                    # tell server to stop
    socket.recv()                           # wait for acknowledgement

if __name__ == "__main__":
    main()
