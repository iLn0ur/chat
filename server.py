import json
from socket import socket, AF_INET, SOCK_STREAM
# import time
from client import get_params


def client_msg_receive(binary_msg):
    client_msg = binary_msg.decode('ascii')
    json_msg = json.loads(client_msg)
    return json_msg


def server_resp():
    server_json = {
        "response": 200,
        "alert": "Необязательное сообщение/уведомление"
    }

    server_str = json.dumps(server_json)
    server_binary = server_str.encode('utf-8')
    return server_binary


def main(addr, p):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((addr, p))
    s.listen(5)

    while True:
        client, addr = s.accept()
        print(f"Получен запрос на соединение от {str(addr)}")
        # timestr = time.ctime(time.time()) + "\n"
        binary_msg = client.recv(1024)
        print(client_msg_receive(binary_msg)["action"])

        client.send(server_resp())
        client.close()


if __name__ == '__main__':
    args = get_params()
    main(args.addr, args.p)
