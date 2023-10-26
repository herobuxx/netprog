import socket
from binascii import hexlify

def conv_ip4():
    for ip_addr in ['127.0.0.1','192.168.54.1']:
        packet_ip_addr = socket.inet_aton(ip_addr)
        unpacket_ip_addr = socket.inet_ntoa(packet_ip_addr)
        print("IP Addr: %s => Packed: %s => UnPacked: %s"
        %(ip_addr, hexlify(packet_ip_addr), unpacket_ip_addr))

if __name__ == '__main__':
    conv_ip4()
