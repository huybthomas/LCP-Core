import logging
import sys
from copy import copy
from termcolor import colored

COLOR_MAPPING = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'white'
}


class Logger(object):
    def __init__(self, to_file=None, to_terminal=False, to_director=None, log_level=logging.INFO):
        logging.basicConfig(level=log_level)
        self.__handlers = []

        if to_terminal:
            colored_formatter = self.ColoredFormatter('%(asctime)s.%(msecs)03d %(levelname)21s' + ' ' + colored('%(process)4s', "magenta", None, ["bold"]) + ' --- [%(name)s] ' + colored('%(funcName)s#%(lineno)d', "cyan", None) + ' : %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
            terminal_handler = logging.StreamHandler(stream=sys.stdout)
            terminal_handler.setLevel(log_level)
            terminal_handler.setFormatter(colored_formatter)
            self.__handlers.append(terminal_handler)

        if to_file:
            file_handler = logging

    def get_logger(self, name):
        logger = logging.getLogger(name)
        logger.propagate = False

        for handler in self.__handlers:
            logger.addHandler(handler)

        return logger

    class ColoredFormatter(logging.Formatter):
        def __init__(self, pattern, datefmt):
            logging.Formatter.__init__(self, pattern, datefmt)

        def format(self, record):
            colored_record = copy(record)
            levelname = colored_record.levelname
            colored_record.levelname = colored(levelname, COLOR_MAPPING.get(levelname, 'white'), None if not levelname == 'CRITICAL' else 'on_red', ['bold'])
            return logging.Formatter.format(self, colored_record)
