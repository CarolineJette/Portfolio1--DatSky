import socket

print("Dette er en klient")

sock = socket.socket(type = socket.SOCK_DGRAM)
#sock.connect(("localhost", 4242))

while True:
    print("Enter message: ", end = "")
    msg = input()
    print("Sending \"{}\" ".format(msg))
    sock.sendto(msg.encode(), ("localhost", 4242))
    reply = sock.recv(1024).decode()
    print("Server replied: {}".format(reply))

