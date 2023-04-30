import json
from socket import socket, AF_INET, SOCK_STREAM
import time
import argparse


def main(addr, p):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((addr, p))
    s.listen(5)

    while True:
        client, addr = s.accept()
        print("Получен запрос на соединение от %s" % str(addr))
        timestr = time.ctime(time.time()) + "\n"

        binary_msg = client.recv(1024)
        client_msg = binary_msg.decode('ascii')
        json_msg = json.loads(client_msg)
        print(json_msg["action"])

        server_json = {
                        "response": 200,
                        "alert":"Необязательное сообщение/уведомление"
        }

        server_str = json.dumps(server_json)
        server_binary = server_str.encode('utf-8')
        client.send(server_binary)
        client.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='start script args')
    parser.add_argument(
        '-addr',
        type=str,
        default='localhost',
        help='addr of server, default localhost'
    )
    parser.add_argument(
        '-p',
        type=int,
        default=7777,
        help='port number, default 7777'
    )
    parser = argparse.ArgumentParser(description='start script args')
    parser.add_argument(
        '-addr',
        type=str,
        default='localhost',
        help='addr of server, default localhost'
    )
    parser.add_argument(
        '-p',
        type=int,
        default=7777,
        help='port number, default 7777'
    )

    args = parser.parse_args()
    main(args.addr, args.p)
