import json
import logging
import sys
from socket import socket, AF_INET, SOCK_STREAM
# import time
from client import get_params
import log.server_config_log
from decorators import log, Log
from select import select


logger = logging.getLogger('server_log')


@log
def client_msg_receive(binary_msg):
    client_msg = binary_msg.decode('utf-8')
    # json_msg = json.load(client_msg)
    logger.debug(f'получено сообщение от клиента {client_msg}')
    return client_msg


@log
def server_resp():
    server_json = {
        "response": 200,
        "alert": "notification"
    }

    server_str = json.dumps(server_json)
    server_binary = server_str.encode('utf-8')
    logger.debug('отправлено сообщение клиенту')
    return server_binary


def listen_sock(a, p):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((a, p))
    s.listen(5)
#    s.settimeout(1)
    return s


def read_requests(read_clients, all_clients):
    """Чтение запросов из списка клиентов"""

    responses = {}

    for client in read_clients:
        try:
            binary_msg = client.recv(1024)
            responses[client] = client_msg_receive(binary_msg)
            logger.info(f"принято сообщение: {responses[client]}")
        except Exception as e:
            logger.info(f"Клиент {client.fileno()} {client.getpeername()} отключился")
            logger.debug(e)
            all_clients.remove(client)

    return responses


def write_responses(requests, readers, all_signed):
    """Эхо-ответ сервера клиентам, от которых были запросы"""

    for client in all_signed:
        # if client in requests:
        try:
            # resp = requests[sock].upper()
            # print(resp)
            for writer in requests:
                client.send(requests[writer].encode('utf-8'))
        except Exception as e:
            logger.info(f"Клиент {client.fileno()} {client.getpeername()} отключился")
            logger.debug(e)
            client.close()
            all_signed.remove(client)
            pass


def main(a, p):

    if not 1023 < p < 65536:
        logger.critical(f'Попытка запуска сервера с указанием неподходящего порта {p}')
        sys.exit()

    logger.info(f'Запущен сервер, порт для подключений: {p}, '
                f'адрес с которого принимаются подключения: {a}. '
                f'Если адрес не указан, принимаются соединения с любых адресов.')

    s = listen_sock(a, p)
    s.settimeout(0.1)
    all_signed = []

    while True:
        try:
            client, a = s.accept()
        except OSError as e:
            logger.debug(e)
        else:
            logger.info(f"Получен запрос на соединение от {client.getpeername()}")
            all_signed.append(client)
        finally:
            wait = 0
            readers = []
            writers = []
            try:
                writers, readers, errors = select(all_signed, all_signed, [], wait)
            except Exception as e:
                logger.debug(e)

            requests = read_requests(writers, all_signed)

            if requests:
                write_responses(requests, readers, all_signed)


if __name__ == '__main__':
    args = get_params()
    main(args.addr, args.p)
