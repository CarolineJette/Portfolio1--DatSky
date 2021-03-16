import socket
import random
import sys
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv)!=2:
    print("Correct usage: script, port number")

Port = int(sys.argv[1])

print("Dette er serveren")
sock.bind(("127.0.0.1", Port))
sock.listen()
#conn, addr = sock.accept()

list_of_clients = []
list_of_bots = []

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = list_of_clients.index(client)
            list_of_clients.remove(client)
            client.close()
            bot = list_of_clients[index]
            broadcast('{} left!'.format(bot).encode('ascii'))
            list_of_bots.remove(bot)
            break
#def clientthread(conn, addr):
#    action = random.choice(["sing", "drink", "clean", "eat", "sleep", "study", "think", "work"])
#    msg = "Host: Do you guys want to {} today? ".format(action)
#    print(msg)
#    conn.sendall(msg.encode())

#    while True:
#        try:
#            answer = conn.recv(1024).decode()
#            if answer:
#                print("<" + addr[0] + "> " + answer)
#                answer_to_send = "<" + addr[0] + "> " + answer
#                broadcast(answer_to_send, conn)
#            else:
#                removeconn(conn)
#        except:
#            continue

def broadcast(msg):
    for client in list_of_clients:
        client.send(msg)
#def broadcast(msg, conn):
#    for client in list_of_clients:
#        if client!=conn:
#            try:
#                client.send(msg)
#            except:
#                client.close()
#                removeconn(client)

#def removeconn(conn):
#    if conn in list_of_clients:
#        list_of_clients.remove(conn)

def receive():
    while True:
        client, addr = sock.accept()
        print("Connected with {}".format(str(addr)))
        client.send('BOT'.encode('ascii'))
        bot = client.recv(1024).decode('ascii')
        list_of_bots.append(bot)
        list_of_clients.append(client)
        print("Bots' name is {}".format(bot))
        broadcast("{} joined!".format(bot).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
#while True:
#    conn, addr = sock.accept()
#    list_of_clients.append(conn)
    #print(addr[0] + " connected")

#    start_new_thread(clientthread, (conn, addr))

#conn.close()
#sock.close()

receive()

#with conn: 
    #print("Connected by ", addr)
    #while True:
        #data = conn.recv(1024)
        #if not data:
         #   break

        #conn.sendall(data)
        #print("Awaiting message...")
        
        #print("Message from {}:{}\nContent: {}".format(addr, port, data.decode()))
        #action = random.choice(["sing", "drink", "clean", "eat", "sleep", "study", "think", "work"])
        #msg = "Host: Can we {}, please? ".format(action)
        #print(msg)
        #data, (addr, port) = conn.recvfrom(1024)
        #conn.sendto(action.encode(), (addr, port))
        #print(addr, port, data.decode())