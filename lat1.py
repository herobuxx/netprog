import socket

def get_hostinfo():
    host_name = socket.gethostname()
    ip_addr = socket.gethostbyname(host_name)
    print("Hostaname : ", host_name)
    print("IP Addrs  : ", ip_addr)

if __name__ == '__main__':
    get_hostinfo()
