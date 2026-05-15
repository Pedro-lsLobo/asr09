import zmq

SERVER_IP = "3.227.138.6"
PEER_IP   = "32.197.15.158"
PORT      = "5678"

def main():
    address = "tcp://" + SERVER_IP + ":" + PORT

    context = zmq.Context()
    socket  = context.socket(zmq.REQ)           # create request socket
    socket.connect(address)                     # connect to remote server
    print("Peer " + PEER_IP + " connected to server at " + address)

    socket.send(b"Hello world")             # send request
    message = socket.recv()                 # block until response
    print("Reply: " + message.decode())     # print result

    socket.send(b"STOP")                    # tell server to stop
    socket.recv()                           # wait for acknowledgement

if __name__ == "__main__":
    main()
