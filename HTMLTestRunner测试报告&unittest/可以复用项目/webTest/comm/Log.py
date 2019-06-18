import os
import logging
import threading
import time
import sys
sys.path.append("..")
import readConfig as readConfig

localReadConfig = readConfig.ReadConfig()


class Log:

    def __init__(self):
        global result, logPath, logFilePath
        result = os.path.join(readConfig.proDir, 'result')
        
        if not os.path.exists(result):
            os.mkdir(result)
        logFilePath = os.path.join(result, str(time.strftime('%Y%m%d%H%M%S', time.localtime())))
        if not os.path.exists(logFilePath):
            os.mkdir(logFilePath)
        logPath = os.path.join(logFilePath, 'result.log')
        self.logger = logging.getLogger()
        # set log level
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s')
        # defined handler
        self.fhandler = logging.FileHandler(logPath)
        self.strhandler = logging.StreamHandler()
        # defined formatter
        
        # set formatter
        self.fhandler.setFormatter(self.formatter)
        self.strhandler.setFormatter(self.formatter) 
        # add handler
        self.logger.addHandler(self.fhandler)
        self.logger.addHandler(self.strhandler)
    def get_logger(self):
        """
        get logger
        :return:
        """
        return self.logger

    def build_start_line(self, name):
        """
        build start line
        :param name:
        :return:
        """
        line = '************' + name + ' START************'
        self.logger.info(line)

    def build_end_line(self, name):
        """
        build end line
        :param name:
        :return:
        """
        line = '************' + name + ' END************'
        self.logger.info(line)

    def get_logfile_path(self):
        """
        get result file path
        :return:
        """
        return logFilePath

    def get_log_path(self):
        """
        get result log path
        :return:
        """
        return logPath

    def get_report_path(self):
        """
        get report file path
        :return:
        """
        report_path = os.path.join(logFilePath, 'report.html')
        return report_path


class MyLog:

    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()
        return MyLog.log

if __name__ == '__main__':
    log = MyLog.get_log()
    logger = log.get_logger()
    logger.info('test info')
    print("")
