import socket
import random
import select
import sys

print("Dette er en klient")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print("Correct usage: script, IP adress, port number, bot")
    exit()

ip = str(sys.argv[1])
port = int(sys.argv[2])

sock.connect((ip, port))

def alice(a, b = None):
        return "I think {} sounds great!".format(a + "ing")

while True:
    socket_list = [sys.stdin, sock]
    read_sockets, write_sockets, error_socket = select.select(socket_list, [], [])

    for sockets in read_sockets:
        msg = sockets.recv(1024).decode()
        print(msg)




sock.close()
#sock.sendall(b"Hello world")
#data = sock.recv(1024)

#while True:
    #print("Enter message: ", end = "")
    #msg = input()
    #print("Sending \"{}\" ".format(msg))
    
    #reply = sock.recv(1024).decode()
    #print("Server replied: {}".format(reply))
    #data, (addr, port) = sock.recvfrom(1024)
    

    #action = random.choice(["work", "play", "eat", "cry", "sleep", "fight"])
    #data, (addr, port) = sock.recvfrom(1024)
    #action = sock.recvfrom(1024).decode()
    #reply = "Alice: {}".format(alice(action))
    #sock.sendto(reply.encode(), ("localhost", 4242))

