import socket
import select
import sys
import errno

HEADER_LENGTH = 10
BYTES = 1024

IP = str(sys.argv[1])
PORT = int(sys.argv[2])
bot = str(sys.argv[3])

my_botname = bot
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(True)

host_msg = client_socket.recv(1024).decode('ascii')
print(host_msg)
botname = my_botname.encode('utf-8')
botname_header = f"{len(botname):<{HEADER_LENGTH}}".encode('utf-8')

client_socket.send(botname_header + botname)

while True:
    message = input("{}: ".format(my_botname))
    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)

    try:
        while True:
            botname_header = client_socket.recv(BYTES)
            if not len(botname_header):
                print("Connection closed by the server")
                sys.exit()

            botname_length = int(botname_header.decode('utf-8').strip())
            botname = client_socket.recv(botname_length).decode('utf-8')

            message_header = client_socket.recv(BYTES)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            print("{}: {}".format(botname, message))

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error', str(e))
            sys.exit()
        continue

    except Exception as e:
        print('General error', str(e))
        sys.exit()


