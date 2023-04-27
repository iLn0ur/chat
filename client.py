from socket import socket, AF_INET, SOCK_STREAM
import time
import json

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 7777))


def form_precense_msg():
    message = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    json_msg = json.dumps(message)
    binary_msg = json_msg.encode('ascii')

    return binary_msg


client.send(form_precense_msg())

tm = client.recv(1024)
client.close()

print("Текущее время: %s" % tm.decode('ascii'))
