import socket

def get_buf_info():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Send
    sndbuf = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Default send Buffer Size: %s" % sndbuf)
    # Receive
    rcvbuf = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print("Default received Buffer Size: %s" % rcvbuf)

if __name__ == '__main__':
    get_buf_info()
