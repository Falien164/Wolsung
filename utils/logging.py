import logging
import os


class Logging:
    def __init__(self):
        log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s',
                                          datefmt='%Y-%m-%d %H:%M:%S')

        log_file = os.path.join(os.getcwd(), "_logs", ".log")
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(log_formatter)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(log_formatter)
        self.app_log = logging.getLogger()
        self.app_log.addHandler(stream_handler)
        self.app_log.addHandler(file_handler)

    def info(self, message):
        self.app_log.setLevel(logging.INFO)
        self.app_log.info(message)

    def debug(self, message):
        self.app_log.setLevel(logging.DEBUG)
        self.app_log.debug(message)

    def warning(self, message):
        self.app_log.setLevel(logging.WARNING)
        self.app_log.warning(message)

    def error(self, message):
        self.app_log.setLevel(logging.ERROR)
        self.app_log.warning(message)