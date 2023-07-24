import socket
import _thread

# Global veriables
PORT = 8001
ADDRESS = ("10.29.60.96", PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(ADDRESS)
CLIENTS = {}


def broadcast_message(data, conn, addr):
    for client in CLIENTS:
        if client != addr[0]:
            print(client)
            # conn.send(("<" + addr[0] + "> " + data).encode())
            CLIENTS[client].send(("<" + addr[0] + "> " + data).encode())
            # s.sendto(("<" + addr[0] + "> " + data).encode(), client)


def server(conn, addr):
    # print(addr[0])
    # broadcast_message("has joined!", conn, addr)
    while True:
        data = conn.recv(1024).decode()
        if data:
            broadcast_message(data, conn, addr)


while True:
    s.listen(6)
    conn, addr = s.accept()
    CLIENTS[addr[0]] = conn
    # print(addr)
    _thread.start_new_thread(server, (conn, addr))
