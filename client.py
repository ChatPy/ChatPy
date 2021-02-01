import socket
import select
import errno
import sys
import threading
import random
import hashlib
from cmdargs import *
from channel import *
from log import *
HEADER_LENGTH = 10
IP = "0.0.0.0"
PORT = 8081
my_username = "Guest" + str(random.randint(0,9999))
channel = "#chat"
log(f'Connecting to {IP}:{PORT}...')
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)
log('Sending username data...')
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)
log('Ready to receive and send messages.')
while True:
    message = input(f"<{my_username}> ")
    if message == "/leave":
      exit()
    if message.startswith("/nick "):
      my_username = args(message)[1]
      continue
    if message.startswith("/join "):
      channel = args(message)[1]
      continue
    if message.startswith("/"):
      continue
    if message:
        message = (channel + "|" + message).encode("utf-8")
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)
    try:
        while True:
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()
            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')
            message_data = decode(message)
            if channel == message_data[0]:
              print(f'<{username}> {message_data[1]}')
    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()
        continue
    except Exception as e:
        print('Reading error: '.format(str(e)))
        sys.exit()
