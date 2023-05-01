from socket import socket, AF_INET, SOCK_STREAM
import time
import json
import argparse


def form_precense():
    message = {
        "action": "presense",
        "time": time.time(),
        "type": "status",
        "user": {
                "account_name": "account_name",
                "status": "Yep, I am here!"
        }
    }
    json_msg = json.dumps(message)
    binary_msg = json_msg.encode('ascii')

    return binary_msg


def form_probe():
    message = {
        "action": "probe",
        "time": time.time(),
        "user": {
            "account": "account_name"
        }
    }
    json_msg = json.dumps(message)
    binary_msg = json_msg.encode('ascii')

    return binary_msg


def form_msg():
    message = {
        "action": "msg",
        "time": time.time(),
        "to": "account_name",
        "from": "account_name",
        "encoding": "ascii",
        "message": "message"
    }
    json_msg = json.dumps(message)
    binary_msg = json_msg.encode('ascii')

    return binary_msg


def form_quit():
    message = {
        "action": "quit",
    }
    json_msg = json.dumps(message)
    binary_msg = json_msg.encode('ascii')

    return binary_msg


def form_authenticate():
    message = {
        "action": "authenticate",
        "time": time.time(),
        "user": {
                "account_name": "acc",
                "password": "pass"
            }

    }
    json_msg = json.dumps(message)
    binary_msg = json_msg.encode('ascii')

    return binary_msg


def form_join():
    message = {
        "action": "join",
        "time": time.time(),
        "room": "#room_name"
    }
    json_msg = json.dumps(message)
    binary_msg = json_msg.encode('ascii')

    return binary_msg


def form_leave():
    message = {
        "action": "leave",
        "time": time.time(),
        "room": "#room_name"
    }
    json_msg = json.dumps(message)
    binary_msg = json_msg.encode('ascii')

    return binary_msg


def get_params():
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

    return parser.parse_args()


def set_connect():
    pass


if __name__ == '__main__':

    args = get_params()
    print(get_params().addr)

    client = socket(AF_INET, SOCK_STREAM)
    client.connect((args.addr, args.p))
    client.send(form_precense())

    tm = client.recv(1024)
    client.close()
    tm_str = tm.decode('utf-8')
    tm_json = json.loads(tm_str)

    print(f'Ответ сервера: {tm_json["response"]}')
