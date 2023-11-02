import sys
import socket
import argparse

def main():
    # Setup args parser
    argpr = argparse.ArgumentParser(description='Socket Error Example')
    argpr.add_argument('--host', action="store", dest="host", required=False)
    argpr.add_argument('--port', action="store", dest="port", type=int, required=False)
    argpr.add_argument('--file', action="store", dest="file", required=False)
    user_args = argpr.parse_args()
    host = user_args.host
    port = user_args.port
    file = user_args.file
    
    # Check if host and port are provided
    if not (host and port):
        print("Error: Both host and port are required.")
        sys.exit(1)

    # try 1
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Error creating socket: %s" % e)
        sys.exit(1)

    # try 2
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        sys.exit(1)
    except socket.error as e:
        print("Connection error: %s" % e)
        sys.exit(1)


    # try 1
    try:
        msg = "GET %s HTTP/1.0\r\n\r\n" % file
        s.sendall(msg.encode('utf-8'))
    except socket.error as e:
        print("Error creating socket: %s" % e)
        sys.exit(1)

    while True:
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print("Error receiving data: %s" % e)
            sys.exit(1)
        if not len(buf):
            break
        sys.stdout.write(buf.decode('utf-8'))

if __name__ == '__main__':
    main()
 