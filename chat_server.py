import socket
import _thread
import uuid
from server import Server
from chatroom import Chatroom
from client import Client
from message import Message

# Global variables
server = Server("10.29.60.96", 8001)

# Sets up host connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((server.ip_address, server.port))

# Initializes clients and chat room
CLIENTS = {}
chatroom = Chatroom("Chat Room", uuid.uuid1())

def broadcast_message(data, addr):
    """Broadcasts a message to all users other than the sender

    :param data: The string message to be sent to other users other than the sender
    :param addr: The IP address of the sender
    
    :return: None
    """

    for client in CLIENTS:
        if client.ip_address != addr[0]:
            print(f"{client.username} just received a message.")
            CLIENTS[client][0].send(("<" + CLIENTS[client][1].username + "> " + data).encode())
            message = Message(CLIENTS[client][1], data)
            chatroom.send(message)

def server(conn, addr):
    """Listens to input from a chatroom user

    :param conn: The connection with the chatroom user
    :param addr: The IP address of the chatroom user
    
    :return: None
    """

    client = None

    while True:
        data = conn.recv(1024).decode().strip()
        
        if data.substr(0, 8) == "USERINFO":
            user_info = data.split()

            client = Client(user_info[1], addr[0], user_info[2], user_info[3])
            CLIENTS[addr[0]].append(client)
            chatroom.add_client(client)

            message = f"{client.username} just joined."
            broadcast_message(message, addr)
        elif data == "EXIT":
            chatroom.delete_client(client)
            CLIENTS[client][0].close()
            
            try:
                CLIENTS.pop(client)
            except KeyError:
                print("Client does not exist.")

            message = f"{client.username} just left."
            broadcast_message(message, addr)
        elif data:
            broadcast_message(data, addr)

# Implements multithreading to listen to up to 6 users simultaneously
while True:
    s.listen(6)
    conn, addr = s.accept()
    CLIENTS[addr[0]] = [conn]
    _thread.start_new_thread(server, (conn, addr))
