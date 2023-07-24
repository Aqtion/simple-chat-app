import socket
import client
import uuid
import server
from subprocess import check_output

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

user = client.Client()
serv = server.Server()

ip_address = check_output(["hostname", "-I"]).strip().decode().split()[1]

serv.port = 8000
serv.ip_address = "10.39.40.234"

username = input("Enter your username")
user.username = username
user.ip_address = ip_address
password = input("Enter your password")
user.password = password
user.uuid = uuid.uuid1()

s.connect((serv.ip_address, serv.port))

while True:
    conn, addr = s.accept()
