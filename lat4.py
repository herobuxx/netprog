import socket
from binascii import hexlify

def scan_service():
    protocol_name = 'tcp'
    for ports in [80, 25]:
        print("Port: %s => Service name: %s" %(ports, socket.getservbyport(ports,protocol_name)))
        print("Port: %s => Service name: %s" %(53, socket.getservbyport(53,'udp')))

if __name__ == '__main__':
    scan_service()
