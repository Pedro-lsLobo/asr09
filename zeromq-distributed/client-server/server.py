import zmq
import sys

def main():
    port = sys.argv[1] if len(sys.argv) > 1 else "12345"

    context = zmq.Context()
    socket  = context.socket(zmq.REP)       # create reply socket
    socket.bind("tcp://*:" + port)          # bind to all interfaces
    print("Server listening on port " + port + " ...")

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
