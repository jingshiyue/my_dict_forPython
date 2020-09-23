import logging.handlers
"""
日志文件分包
"""



class FinalLogger:
    logger = None
    log_file = r"D:\work\debug.log"
    log_max_byte = 10 * 1024 
    log_backup_count = 10

    @staticmethod
    def getLogger():
        if FinalLogger.logger is not None:
            return FinalLogger.logger
        FinalLogger.logger = logging.Logger("loggingmodule.FinalLogger")
        log_handler = logging.handlers.RotatingFileHandler(filename = FinalLogger.log_file,\
                                                            maxBytes = FinalLogger.log_max_byte,\
                                                            backupCount = FinalLogger.log_backup_count)
        log_fmt = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")
        log_handler.setFormatter(log_fmt)
        FinalLogger.logger.addHandler(log_handler)
        FinalLogger.logger.setLevel(logging.DEBUG)

        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        # formatter = logging.Formatter("%asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")
        formatter = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")
        console.setFormatter(formatter)
        FinalLogger.logger.addHandler(console)
        return FinalLogger.logger


class mylog():
    def __init__(self,log_file="debug.log",log_max_byte=150*1024*1024,log_backup_count=5):
        self.logger = None
        self.log_file = log_file
        self.log_max_byte = log_max_byte
        self.log_backup_count = log_backup_count
    
    def getLogger(self):
        if self.logger is not None:
            return self.logger
        self.logger = logging.Logger("loggingmodule.FinalLogger")
        log_handler = logging.handlers.RotatingFileHandler(filename = self.log_file,\
                                                            maxBytes = self.log_max_byte,\
                                                            backupCount = self.log_backup_count)
        log_fmt = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")
        log_handler.setFormatter(log_fmt)
        self.logger.addHandler(log_handler)
        self.logger.setLevel(logging.DEBUG)

        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        # formatter = logging.Formatter("%asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")
        formatter = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")
        console.setFormatter(formatter)
        self.logger.addHandler(console)
        return self.logger



if __name__ == "__main__":
    logger = FinalLogger.getLogger()
    while 1:
        logger.debug("this is a debug msg!")
        logger.info("this is a info msg!")
        logger.warning("this is a warn msg!")
        logger.error("this is a error msg!")
        logger.critical("this is a critical msg!")

