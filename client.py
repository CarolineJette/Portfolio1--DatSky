import socket
import random

print("Dette er en klient")

sock = socket.socket(type = socket.SOCK_DGRAM)
#sock.connect(("localhost", 4242))

while True:
    #print("Enter message: ", end = "")
    #msg = input()
    #print("Sending \"{}\" ".format(msg))
    
    #reply = sock.recv(1024).decode()
    #print("Server replied: {}".format(reply))
    def alice(a, b = None):
        return "I think {} sounds great!".format(a + "ing")

    action = random.choice(["work", "play", "eat", "cry", "sleep", "fight"])
    reply = "Alice: {}".format(alice(action))
    sock.sendto(reply.encode(), ("localhost", 4242))

