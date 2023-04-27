from socket import socket, AF_INET, SOCK_STREAM
import time


s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', 7777))
s.listen(5)

while True:
    client, addr = s.accept()
    print("Получен запрос на соединение от %s" % str(addr))
    timestr = time.ctime(time.time()) + "\n"

    binary_msg = client.recv(1024)
    json_msg = binary_msg.decode('ascii')

    print(json_msg)

    client.send(timestr.encode('ascii'))
    client.close()
