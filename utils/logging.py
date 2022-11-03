import logging

class Logger:
    def __init__(self):
        log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s',
                                          datefmt='%d/%m/%Y %H:%M:%S')
        logFile = '.log'

        # Setup File handler
        file_handler = logging.FileHandler(logFile)
        file_handler.setFormatter(log_formatter)

        # Setup Stream Handler (i.e. console)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(log_formatter)

        # Add both Handlers
        self.app_log = logging.getLogger('root')
        self.app_log.addHandler(file_handler)
        self.app_log.addHandler(stream_handler)
        # Get our logger

    def info(self, message):
        self.app_log.setLevel(logging.INFO)
        self.app_log.info(message)

    def debug(self, message):
        self.app_log.setLevel(logging.DEBUG)
        self.app_log.debug(message)

    def warning(self, message):
        self.app_log.setLevel(logging.WARNING)
        self.app_log.warning(message)