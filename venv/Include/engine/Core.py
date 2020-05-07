import socket
import select
import time
import sys
buffer_size = 4096
delay = 0.0001
forward_to = {}
class Forward:
    def __init__(self):
        self.forward = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def start(self, host, port):
        try:
            self.forward.connect((host,port))
            return self.forward
        except Exception as e:
            print(e)
            return False
class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((host,port))
        self.server.listen(200)
