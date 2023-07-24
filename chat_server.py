import socket
import _thread
import server

# Global veriables
serv = server.SERVER("10.29.60.96", 8001)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((serv.ip_address, serv.port))
CLIENTS = {}


def broadcast_message(data, addr):
    for client in CLIENTS:
        if client != addr[0]:
            print(client)
            # conn.send(("<" + addr[0] + "> " + data).encode())
            CLIENTS[client][0].send(("<" + CLIENTS[client][1] + "> " + data).encode())
            # s.sendto(("<" + addr[0] + "> " + data).encode(), client)


def server(conn, addr):
    # print(addr[0])
    # broadcast_message("has joined!", conn, addr)
    while True:
        data = conn.recv(1024).decode()
        if data.substr(0, 8) == "USERINFO":
            user_info = data.split(" ")
            CLIENTS[addr[0]].append(user_info[1])
            CLIENTS[addr[0]].append(user_info[2])
        elif data:
            broadcast_message(data, addr)


while True:
    s.listen(6)
    conn, addr = s.accept()
    CLIENTS[addr[0]] = [conn]
    # print(addr)
    _thread.start_new_thread(server, (conn, addr))
