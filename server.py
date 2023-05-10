import json
import logging
import sys
from socket import socket, AF_INET, SOCK_STREAM
# import time
from client import get_params
import log.server_config_log
from decorators import log, Log


logger = logging.getLogger('server_log')


@Log()
def client_msg_receive(binary_msg):
    client_msg = binary_msg.decode('ascii')
    json_msg = json.loads(client_msg)
    logger.debug('получено сообщение от клиента')
    return json_msg


@Log()
def server_resp():
    server_json = {
        "response": 200,
        "alert": "notification"
    }

    server_str = json.dumps(server_json)
    server_binary = server_str.encode('utf-8')
    logger.debug('отправлено сообщение клиенту')
    return server_binary


def main(addr, p):

    if not 1023 < p < 65536:
        logger.critical(f'Попытка запуска сервера с указанием неподходящего порта {p}')
        sys.exit()

    logger.info(f'Запущен сервер, порт для подключений: {p}, '
                f'адрес с которого принимаются подключения: {addr}. '
                f'Если адрес не указан, принимаются соединения с любых адресов.')
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((addr, p))
    s.listen(5)

    while True:
        client, addr = s.accept()
        logger.info(f"Получен запрос на соединение от {str(addr)}")
        # timestr = time.ctime(time.time()) + "\n"
        binary_msg = client.recv(1024)
        logger.info(client_msg_receive(binary_msg)["action"])

        client.send(server_resp())
        client.close()


if __name__ == '__main__':
    args = get_params()
    main(args.addr, args.p)
