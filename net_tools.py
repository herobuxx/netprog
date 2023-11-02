import sys
import socket
import argparse

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def socket_timeout():
    print("")
    print("###########################################")
    print("# * Show timeout info                     #")
    print("###########################################")
    print("")
    print("Default Socket Timeout: %s" % (s.gettimeout()))
    s.settimeout(100)
    print("Current Socket Timeout: %s" % (s.gettimeout()))

def get_buf_info():
    print("")
    print("###########################################")
    print("# * Show Buffer Size info                 #")
    print("###########################################")
    print("")
    sndbuf = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Default send Buffer Size: %s" % sndbuf)
    rcvbuf = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print("Default received Buffer Size: %s" % rcvbuf)

def edit_buf_size():
    print("")
    print("###########################################")
    print("# * Editing Buffer Size                   #")
    print("###########################################")
    print("")
    get_buf_info()
    SEND_BUF_SIZE = int(input("Input new send buffer size: "))
    RECV_BUF_SIZE = int(input("Input new receive buffer size: "))
    print("")
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUF_SIZE)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)
    sndbuf_new = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    rcvbuf_new = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print("Updated send Buffer Size: %s" % sndbuf_new)
    print("Updated received Buffer Size: %s" % rcvbuf_new)

def error_handler():
    print("")
    print("###########################################")
    print("# * Errot Handler                         #")
    print("###########################################")
    print("")
    host = str(input("Input Hostname: "))
    port = int(input("Input Port Number: "))
    file = str(input("Input filename: "))
    print("")

    if not (host and port):
        print("Error: Both host and port are required.")
        sys.exit(1)

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Error creating socket: %s" % e)
        sys.exit(1)

    try:
        s.connect((host, int(port)))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        sys.exit(1)
    except socket.error as e:
        print("Connection error: %s" % e)
        sys.exit(1)

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
    print("")


def main():
    parser = argparse.ArgumentParser(description='Socket Operations Example')
    parser.add_argument('--check-error', '-c', action='store_true', help='Call error_handler()')
    parser.add_argument('--edit-buffer', '-e', action='store_true', help='Call edit_buf_size()')
    parser.add_argument('--get-buffer', '-i', action='store_true', help='Call get_buf_info()')
    parser.add_argument('--timeout', '-t', action='store_true', help='Call socket_timeout()')
    args = parser.parse_args()

    if args.check_error:
        error_handler()
    elif args.edit_buffer:
        edit_buf_size()
    elif args.get_buffer:
        get_buf_info()
    elif args.timeout:
        socket_timeout()
    else:
        print("No valid option selected. Use --check-error, --edit-buffer, --get-buffer, or --timeout.")

if __name__ == '__main__':
    main()
