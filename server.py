import socket
import sys
import random

if len(sys.argv)!=2:
    print("Correct usage: script, port number")
    exit()

IP = "127.0.0.1"
Port = int(sys.argv[1])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, Port))
server_socket.listen()

connected = []
stop_while = False
while not stop_while:
    client_socket, client_address = server_socket.accept()
    connected.append(client_socket)
    message = input("Do you want to connect more clients, y/n? ")
    if message == 'n':
        stop_while = True

action = random.choice(["sing", "drink", "clean", "eat", "sleep", "study", "think", "work", "party", "scream", "steal", "beat", "catch", "cry"])
host_msg = "Host: Do you guys want to {} today? ".format(action)
print(host_msg)

for i in connected:
    i.send(host_msg.encode())
for i in connected:
    message = i.recv(1024).decode()
    print(message)
    for r in connected:
        if r != i:
            r.send(b"Bot:" + message.encode())
