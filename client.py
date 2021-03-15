import socket
import random
import select
import sys

print("Dette er en klient")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 4:
    print("Correct usage: script, IP adress, port number, bot")
    exit()

ip = str(sys.argv[1])
port = int(sys.argv[2])
#bot_str = str(sys.argv[3])
#bot={'bot_str':bot_str}
bot = str(sys.argv[3])

dispatcher = { 'bot' : bot }
def call_func(x, func):
    try:
        return dispatcher[func](x)
    except:
        return "Invalid function"
sock.connect((ip, port))

def amy(a, b = None):
        return "Amy: I think {} sounds great!".format(a + "ing")

while True:
    socket_list = [sys.stdin, sock]
    read_sockets, write_sockets, error_socket = select.select(socket_list, [], [])

    for sockets in read_sockets:
        msg = sockets.recv(1024).decode()
        print(msg)
        split_msg = msg.split()
        action = split_msg[6]
        reply = "{}".format(call_func(action, 'bot'))
        print(reply)
        sock.sendto(reply.encode(), ("localhost", 4242))

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
    

