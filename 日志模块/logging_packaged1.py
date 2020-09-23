import logging.handlers
"""
日志文件分包， 

一个进程下的其他py文件，用import logging，
logging.debug()直接使用，而不用再配置log

"""


class mylog():
    def __init__(self,log_file="debug.log",log_max_byte=150*1024*1024,log_backup_count=5):
        self.logger = None
        self.log_file = log_file
        self.log_max_byte = log_max_byte
        self.log_backup_count = log_backup_count
    
    def getLogger(self):
        if self.logger is not None:
            return self.logger
        self.logger = logging.getLogger()   #一个进程下的其他线程文件，用import logging，logging.debug(xxx),直接使用。
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
    mylog = mylog(log_max_byte=2*1024).getLogger()
    while 1:
        mylog.debug("yes")
        mylog.debug("no")

