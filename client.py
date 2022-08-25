import socket

HOST = "127.0.0.1"
PORT = 6650
FORMAT = "utf-8"
ADDR = (HOST, PORT)
DISCONNECT_MSG = "!DISCONNECT"
HEADER = 64

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("Hellllllllllllo")
input()
send(DISCONNECT_MSG)
