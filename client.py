import socket
import sys
import random
import time

#The client program takes in 3 command line parameters in addition to the script
if len(sys.argv) != 4:
    print("Correct usage: script, IP adress, port number, bot")
    exit()

IP = str(sys.argv[1])
PORT = int(sys.argv[2])
bot = str(sys.argv[3])

#Creates a TCP socket and connects to the ip address and port given as parameters
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

#Lists with good/bad/random actions
good_things = ["party", "drink", "scream", "eat", "catch", "sing", "sleep", "think"]
bad_things = ["cry", "steal", "beat", "clean", "study", "work"]
random_action = random.choice(["die", "paint a wall green", "wash our clothes", "kick a ball", "buy some popcorn"])

#Bot functions
def amy(a):
    if a in bad_things:
        return "Amy: I don't think {} is such a great idea... Can't we do anything else, such as {}?".format(a + "ing", random.choice(good_things))
    else:
        return "Amy: I think {} sounds great!".format(a + "ing")
def jake(a, b = None):
    if a in bad_things:
        return "Jake: Omg, {} is the beeest!".format(a + "ing")
    else:
        return "Jake: Omg, {} is laaame, let's go {} instead".format(a + "ing", b)
def roza(a, b):
    return "Roza: I will rather {} than {}, but whatever...".format(b, a)
def holt(a):
    return "Captain Holt: I don't appreciate {}.".format(a + "ing")


while True:
    host_msg = client_socket.recv(1024).decode('ascii')
    if "Bot:" in host_msg:
        print(host_msg[4:])
        continue
    else:
        print(host_msg)

    #Trying to get the action from the host message
    try:
        split_msg = host_msg.split()
        action = split_msg[6]
    except:
        exit()

    random_action = random.choice(["sleep", "paint a wall", "wash my clothes", "kick a ball"])

    #Calls the bot functions dependent on the bot parameter
    if bot == 'Amy':
        message = "{}".format(amy(action))
    elif bot == 'Jake':
        message = "{}".format(jake(action, random_action))
    elif bot == 'Roza':
        message = "{}".format(roza(action, random_action))
    elif bot == 'Holt':
        message = "{}".format(holt(action))
    else:
        message = "Host: {} the Bot isn't with us today".format(bot)

    client_socket.send(message.encode())
    print(message)

#Code by Caroline Sofie Jetteberg, s313564 OsloMet