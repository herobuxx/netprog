import socket

def test_sock_to():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Default Socket Timeout: %s" % (s.gettimeout()))  # Corrected line
    s.settimeout(100)
    print("Current Socket Timeout: %s" % (s.gettimeout()))  # Corrected line

if __name__ == '__main__':
    test_sock_to()
