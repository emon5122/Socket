import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
FORMAT = "utf-8"
ADDR = (HOST, PORT)
DISCONNECT_MSG = "!DISCONNECT"
HEADER = 64

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Message Recieved".encode(FORMAT))
    conn.close()


def start():
    server.listen()
    print(f"[Listening] Server is listening on {HOST}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() -1}")


print("[STARTING server is starting]")
start()
