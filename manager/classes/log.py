"""
Some things for the logging
"""
import logging
from colored import Fore, Style, Back

CODENAME = 'ndeploy'


NDEPLOY_TAG = f'[{Fore.blue}{CODENAME}{Style.reset}]'
INFO_TAG = f'[{Fore.cyan}info{Style.reset}]'
WARN_TAG = f'[{Fore.yellow}warn{Style.reset}]'
ERROR_TAG = f'[{Fore.red}error{Style.reset}]'
CRITICAL_TAG = f'[{Fore.magenta}critical{Style.reset}]'
DEBUG_TAG = f'[{Fore.light_green}debug{Style.reset}]'


class ColoredFormatter(logging.Formatter):
    """
    ColoredFormatter class.
    """

    def format(self, record):
        """Apply a format to a message.

        Args:
            record (LogRecord): The log record.
        """
        message = record.getMessage()
        name = f'{Fore.light_gray}{Back.cyan} {record.name} {Style.reset}'

        tag = '[log]'

        text_message = f'{message}'

        if record.levelname == 'INFO':
            tag = INFO_TAG
            text_message = f'{Style.italic}{message}{Style.reset}'
        elif record.levelname == 'WARNING':
            tag = WARN_TAG
            text_message = f'{Style.underline}{message}{Style.reset}'
        elif record.levelname == 'ERROR':
            tag = ERROR_TAG
            text_message = f'{Style.blink}{Fore.light_red}{message}{Style.reset}'
        elif record.levelname == 'CRITICAL':
            tag = CRITICAL_TAG
            text_message = f'{Back.light_red}{message}{Style.reset}'
        elif record.levelname == 'DEBUG':
            tag = DEBUG_TAG
            text_message = f'{Fore.dark_gray}{message}{Style.reset}'
        else:
            text_message = f'{message}'

        text = f'{name} {tag}'

        text += f' {text_message}'

        return text


class NDeployLogger(logging.getLoggerClass()):
    """NDeployLogger"""
    def __init__(self, name: str, level: int | str = 0) -> None:
        super().__init__(name, level)
        formatter = ColoredFormatter()
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.addHandler(handler)


logger = NDeployLogger(CODENAME)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    logger.info('info')
    logger.debug('debug')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')
