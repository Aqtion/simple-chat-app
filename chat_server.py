import socket
import server

# Global veriables
PORT = 8000
ADDRESS = ("", PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDRESS)
CLIENTS = {}

serv = server.Server()


def broadcast_message(data, conn, sender):
    for client in CLIENTS:
        if client.ip_address != sender:
            conn.send("<" + {client.username} + "> " + data.encode())


while True:
    conn, addr = s.accept()
    if not CLIENTS[addr]:
        broadcast_message("has joined!", conn, addr)
        CLIENTS[addr] = conn
    data = conn.recv(1024)
    broadcast_message(data, conn, addr)
