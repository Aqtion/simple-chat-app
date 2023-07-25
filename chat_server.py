import socket
import _thread
import server
import client

# Global veriables
serv = server.Server("10.29.60.96", 8001)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((serv.ip_address, serv.port))
CLIENTS = {}


def broadcast_message(data, addr):
    for client in CLIENTS:
        if client != addr[0]:
            connection = CLIENTS[client][0]
            user = CLIENTS[client][1]
            message = message.Message(user, data)
            connection.send(message.create_message())


def server(conn, addr):
    # print(addr[0])
    # broadcast_message("has joined!", conn, addr)
    while True:
        data = conn.recv(1024).decode()
        if data.substr(0, 8) == "USERINFO":
            user_info = data.split(" ")
            user = client.Client(user_info[1], str(addr[0]), user_info[3], user_info[2])
            CLIENTS[addr[0]].append(user)
        elif data:
            broadcast_message(data, addr)


while True:
    s.listen(6)
    conn, addr = s.accept()
    CLIENTS[addr[0]] = [conn]
    # print(addr)
    _thread.start_new_thread(server, (conn, addr))
