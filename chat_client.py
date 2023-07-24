import socket
import uuid
from subprocess import check_output
from client import Client
from server import Server
import _thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 8001
IP_ADDRESS = "10.29.60.96"  # IP_ADDRESS = check_output(["hostname", "-I"]).strip().decode().split()[1]

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
    while True:
        send_message = input()
        print("<" + client.username + "> " + send_message)
        s.send(send_message.encode())


_thread.start_new_thread(listen, ())

while True:
    message = s.recv(2048)
    print(message.decode())
