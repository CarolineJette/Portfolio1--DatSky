import socket
import random
import sys
import _thread

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv)!=2:
    print("Correct usage: script, port number")

Port = int(sys.argv[1])

print("Dette er serveren")
sock.bind(("0.0.0.0", Port))
sock.listen()
#conn, addr = sock.accept()

list_of_clients = []

def clientthread(conn, addr):
    action = random.choice(["sing", "drink", "clean", "eat", "sleep", "study", "think", "work"])
    msg = "Host: Can we {}, please? ".format(action)
    print(msg)
    conn.sendall(msg.encode())

    while True:
        try:
            answer = conn.recv(1024)
            if answer:
                print("<" + addr[0] + "> " + answer)
                answer_to_send = "<" + addr[0] + "> " + answer
                broadcast(answer_to_send, conn)
            else:
                remove(conn)
        except:
            continue

def broadcast(msg, conn):
    for client in list_of_clients:
        if client!=conn:
            try:
                client.send(msg)
            except:
                client.close()
                remove(client)

def removeconn(conn):
    if conn in list_of_clients:
        list_of_clients.remove(conn)

while True:
    conn, addr = sock.accept()
    list_of_clients.append(conn)
    print(addr[0] + " connected")

    _thread.start_new_thread(clientthread, (conn, addr))

conn.close()
sock.close()

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