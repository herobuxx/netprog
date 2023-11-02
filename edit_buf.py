import socket

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def edit_buf_size():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Show before editing
    sndbuf = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    rcvbuf = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print("Default send Buffer Size: %s" % sndbuf)
    print("Default received Buffer Size: %s" % rcvbuf)

    # Update Buf size
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUF_SIZE)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)
    sndbuf_new = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    rcvbuf_new = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print("Updated send Buffer Size: %s" % sndbuf_new)
    print("Updated received Buffer Size: %s" % rcvbuf_new)

if __name__ == '__main__':
    edit_buf_size()
