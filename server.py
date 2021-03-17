import socket
import select
import sys
import random

HEADER_LENGTH = 10
IP = "127.0.0.1"
Port = int(sys.argv[1])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, Port))
server_socket.listen()

sockets_list = [server_socket]

clients = {}


def receive_message(client_socket):
    try:
        message_header = client_socket.recv(1024)

        if not len(message_header):
            return False
        
        message_length = int(message_header.decode('utf-8'))
        return {"header": message_header, "data": client_socket.recv(message_length)}

    except:
        return False


while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            action = random.choice(["sing", "drink", "clean", "eat", "sleep", "study", "think", "work"])
            host_msg = "Host: Do you guys want to {} today? ".format(action)
            print(host_msg)
            client_socket.sendall(host_msg.encode('ascii'))

            bot = receive_message(client_socket)
            if bot is False:
                continue
            
            sockets_list.append(client_socket)
            clients[client_socket] = bot

            print("{} joined the chat! Address: {}:{}".format(bot['data'].decode('utf-8'), client_address[0], client_address[1]))
        
        else:
            message = receive_message(notified_socket)
            
            if message is False:
                print("Closed connection from {}".format(clients[notified_socket]['data'].decode('utf-8')))
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            
            bot = clients[notified_socket]
            print("{}: {}".format(bot['data'].decode('utf-8'), message['data'].decode('utf-8')))

            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(bot['header'] + bot['data'] + message['header'] + message['data'])
    
    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
