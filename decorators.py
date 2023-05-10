import sys
import logging
import log.client_config_log
import log.server_config_log
import traceback

# метод определения модуля, источника запуска.
# Метод find () возвращает индекс первого вхождения искомой подстроки,
# если он найден в данной строке.
# Если его не найдено, - возвращает -1.
# os.path.split(sys.argv[0])[1]
if sys.argv[0].find('client') == -1:
    logger = logging.getLogger('server_log')
else:
    logger = logging.getLogger('client_log')


def log(func_to_log):
    """Функция-декоратор"""
    def log_saver(*args, **kwargs):
        """Обертка"""
        ret = func_to_log(*args, **kwargs)
        logger.debug(f'Была вызвана функция {func_to_log.__name__} '
                     f'из функции {traceback.format_stack()[0].strip().split()[-1]}.')
        return ret
    return log_saver


class Log:
    """Класс-декоратор"""
    def __call__(self, func_to_log):
        def log_saver(*args, **kwargs):
            """Обертка"""
            ret = func_to_log(*args, **kwargs)
            logger.debug(f'Была вызвана функция {func_to_log.__name__} '
                         f'из функции {traceback.format_stack()[0].strip().split()[-1]}.')
            return ret
        return log_saver
