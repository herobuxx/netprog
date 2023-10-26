import socket

def check_host(remote_host):
    try:
        print("IP Address of",(remote_host,socket.gethostbyname(remote_host)))
    except socket.error as err_msg:
        print(remote_host +":", err_msg)

if __name__ == '__main__':
    check_host("herobuxx.come")
