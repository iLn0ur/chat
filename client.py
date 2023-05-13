from socket import socket, AF_INET, SOCK_STREAM
import time
import json
import argparse
import logging
import log.client_config_log
from decorators import log


logger = logging.getLogger('client_log')


@log
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
    logger.info('сформировано сообщение')
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


@log
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


@log
def set_connect(addr, p):
    client_connect = socket(AF_INET, SOCK_STREAM)
    client_connect.connect((addr, p))
    return client_connect


if __name__ == '__main__':

    args = get_params()

    client = set_connect(args.addr, args.p)
    status = input("send or receive?(s, r)")
    if status == 's':
        while True:
            msg = input('Ваше сообщение: ')
            if msg == 'q':
                client.send(msg.encode('utf-8'))
                client.close()
                break
            client.send(msg.encode('utf-8'))
            logger.info(f'сообщение: {msg}')

    else:
        while True:
            data = client.recv(1024).decode('utf-8')
            print(f'Ответ сервера: {data}')
            # if data == 'q':
            #     client.close()
            #     break

