import socket
import uuid
import _thread
from subprocess import check_output
from client import Client
from server import Server
from message import Message
import _thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Sets the default port to 8000, and the local IP address to 10.29.60.96
PORT = 8000
IP_ADDRESS = "10.29.60.96"

# Determines the local IP address
# IP_ADDRESS = check_output(["hostname", "-I"]).strip().decode().split()[1]

# Inputs username and password, generates uuid
username = input("Enter your username")
password = input("Enter your password")
uuid = uuid.uuid1()

# Initializes Client and Server instances
user = Client(username, IP_ADDRESS, password, uuid)
server = Server(IP_ADDRESS, PORT)

# Connects to the server
s.connect((server.ip_address, server.port))

def listen():
    """Listens for user input to send to the chatroom
    
    :return: None
    """
    while True:
        send_message = input()
        raw_message = Message(user, send_message)
        print(raw_message.create_message().decode())
        s.send(send_message.encode())

# Starts a thread to listen for user input
_thread.start_new_thread(listen, ())

# Receives chatroom messages
while True:
    mess = s.recv(2048)
    print(mess.decode())