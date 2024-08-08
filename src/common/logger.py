
import logging.handlers
import threading

from common.const import LOG_ALL_FILE, LOG_ERROR_FILE, LOG_DEBUG_FILE, LOG_FORMAT


class DebugFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.DEBUG


class Logger:
    _instance = None
    _instance_lock = threading.Lock()
    logger = logging.getLogger('main')

    def __init__(self):
        self.logger.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter(fmt=LOG_FORMAT)

        # 创建文件处理器，每个日志文件每天转存一次，最多保留100个日志文件
        file_handler = logging.handlers.RotatingFileHandler(
            LOG_ALL_FILE, maxBytes=1024 * 1024 * 3, backupCount=100, encoding='utf-8'
        )
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)

        # 错误日志记录器
        error_handler = logging.handlers.RotatingFileHandler(
            LOG_ERROR_FILE, maxBytes=1024 * 1024 * 3, backupCount=100, encoding='utf-8'
        )
        error_handler.setLevel(logging.WARNING)
        error_handler.setFormatter(formatter)

        # debug日志记录器
        debug_handler = logging.handlers.RotatingFileHandler(
            LOG_DEBUG_FILE, maxBytes=1024 * 1024 * 3, backupCount=100, encoding='utf-8'
        )
        debug_handler.setLevel(logging.DEBUG)
        debug_handler.setFormatter(formatter)
        debug_handler.addFilter(DebugFilter())

        # 再创建一个handler，用于输出到控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(file_handler)
        self.logger.addHandler(error_handler)
        self.logger.addHandler(debug_handler)
        self.logger.addHandler(stream_handler)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._instance_lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def set_log_level(cls, log_level):
        cls.logger.setLevel(log_level)


logger = Logger().logger


if __name__ == '__main__':
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
