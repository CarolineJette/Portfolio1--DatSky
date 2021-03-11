import socket

print("Dette er serveren")

sock = socket.socket(type = socket.SOCK_DGRAM)

sock.bind(("0.0.0.0", 4242))

while True:
    print("Awaiting message...")
    data, (addr, port) = sock.recvfrom(1024)
    print("Message from {}:{}\nContent: {}".format(addr, port, data.decode()))
    print("Enter reply: ", end = "")
    reply=input()
    sock.sendto(reply.encode(), (addr, port))

