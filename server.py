import socket
import sys
import random

#The server program takes in 1 command line parameter, port number, in addition to the script
if len(sys.argv)!=2:
    print("Correct usage: script, port number")
    exit()

IP = "127.0.0.1"
Port = int(sys.argv[1])

#Creates a TCP socket and bind to localhost (127.0.0.1) and the port given as parameter
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, Port))
server_socket.listen()

connected = []

stop_while = False

while not stop_while:
    #Accepts as many incoming connections the user wants
    client_socket, client_address = server_socket.accept()
    connected.append(client_socket)
    message = input("Do you want to connect more clients, y/n? ")
    if message == 'n':
        stop_while = True

#The message from host/server that the bots will be to replying to
action = random.choice(["sing", "drink", "clean", "eat", "sleep", "study", "think", "work", "party", "scream", "steal", "beat", "catch", "cry"])
host_msg = "Host: Do you guys want to {} today? ".format(action)
print(host_msg)

#Runs through the connections/clients and sends/receives the bots'replies
for i in connected:
    i.send(host_msg.encode())
for i in connected:
    message = i.recv(1024).decode()
    print(message)
    for r in connected:
        if r != i:
            r.send(b"Bot:" + message.encode())


#Code by Caroline Sofie Jetteberg, s313564 OsloMet