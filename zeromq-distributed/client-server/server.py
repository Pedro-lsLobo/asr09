import zmq

SERVER_IP = "3.227.138.6"
PORT      = "5678"

def main():
    context = zmq.Context()
    socket  = context.socket(zmq.REP)           # create reply socket
    socket.bind("tcp://*:" + PORT)              # bind to all interfaces
    print("Server " + SERVER_IP + " listening on port " + PORT + " ...")

    while True:
        message = socket.recv()             # wait for incoming message
        if "STOP" not in str(message):      # if not a stop command...
            reply = message.decode() + "*"  # append "*" to message
            socket.send(reply.encode())     # send reply back
        else:
            socket.send(b"OK")              # acknowledge stop
            break                           # exit loop

    print("Server stopped.")

if __name__ == "__main__":
    main()
