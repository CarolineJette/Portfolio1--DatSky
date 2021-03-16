import socket
import random
import select
import sys
import threading

print("Dette er en klient")

if len(sys.argv) != 4:
    print("Correct usage: script, IP adress, port number, bot")
    exit()

ip = str(sys.argv[1])
port = int(sys.argv[2])
bot = str(sys.argv[3])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, port))

def amy(a, b = None):
        return "I think {} sounds great!".format(a + "ing")

def jake(a, b = None):
        return "Omg, {} is laaame".format(a + "ing")

def receive():
    while True:
        try:
            message = sock.recv(1024).decode('ascii')
            if message == 'BOT':
                sock.send(bot.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured!")
            sock.close()
            break

def write():
    while True:
        if bot == "amy":
            message = '{}: {}'.format(bot, amy(action))

        if bot == "jake":
            message = '{}: {}'.format(bot, jake(action))
        
        sock.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()


#while True:
#    socket_list = [sys.stdin, sock]
#    read_sockets, write_sockets, error_socket = select.select(socket_list, [], [])

#    for sockets in read_sockets:
#        msg = sockets.recv(1024).decode()
#        print(msg)
#        split_msg = msg.split()
#        action = split_msg[6]
        
        
#    for sockets in write_sockets:
#        if bot == "amy":
#            reply = "{}".format(amy(action))
#            print("Me: " + reply)
#            sock.sendto(("Amy: " + reply).encode(), ("localhost", 4242))
#        if bot == "jake":
#            reply = "{}".format(jake(action))
#            print("Me: " + reply)
#            sock.sendto(("Jake: " + reply).encode(), ("localhost", 4242))

#sock.close()


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
    

