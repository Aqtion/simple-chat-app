import socket
import uuid
from subprocess import check_output
from client import Client
from server import Server
import message
import _thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 8001
IP_ADDRESS = "10.29.60.96"

client = Client()
server = Server(IP_ADDRESS, PORT)

client.ip_address = IP_ADDRESS
client.uuid = uuid.uuid1()

username = input("Enter your username")
client.username = username

password = input("Enter your password")
client.password = password

s.connect((server.ip_address, server.port))


def listen():
    user_info_string = (
        "USERINFO " + client.username + " " + client.uuid + " " + client.password
    )
    s.send(user_info_string.encode())
    while True:
        send_message = input()
        message = message.Message(client, send_message)
        print(message.create_message())
        s.send(send_message.encode())


_thread.start_new_thread(listen, ())

while True:
    message = s.recv(2048)
    print(message.decode())
