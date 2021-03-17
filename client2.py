import socket
import sys

IP = str(sys.argv[1])
PORT = int(sys.argv[2])
bot = str(sys.argv[3])

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

def amy(a, b = None):
        return "Amy: I think {} sounds great!".format(a + "ing")
def jake(a, b = None):
        return "Jake: Omg, {} is laaame".format(a + "ing")


while True:
    host_msg = client_socket.recv(1024).decode('ascii')
    if "Bot:" in host_msg:
        print(host_msg[4:])
        continue
    else:
        print(host_msg)

    try:
        split_msg = host_msg.split()
        action = split_msg[6]
    except:
        exit()

    if bot == 'Amy':
        message = "{}".format(amy(action))
    elif bot == 'Jake':
        message = "{}".format(jake(action))
    else:
        message = "Ingen av botene sier noe"

    client_socket.send(message.encode())
    print(message)