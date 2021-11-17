import socket
import sys

port = int(sys.argv[1])
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', port))

while True:
    data, address = sock.recvfrom(65538)
    text = data.decode('ascii')
    print('Connection from Client{} says {}'.format(address, text))
    text = 'Your data was {} bytes long'.format(len(data))
    data = text.encode('ascii')
    sock.sendto(data, address)
