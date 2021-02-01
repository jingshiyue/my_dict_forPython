# @echo off
# SETLOCAL ENABLEDELAYEDEXPANSION

# REM cd D:\test\jiangyi\PDM\exe
# set path=%cd%\exe
# echo %path%
# pause
# for %%i in (
    # DRAstaticFetch.py
    # EPCHWstasticFetch.py
    # ERMSCStasticFetch.py
    # gongdanStatic.py
    # HSSstaticsFetch.py
    # HWGMSCstasticFetch.py
    # HWMSCStasticFetch.py
    # backendProcessInit.py
    # portsTrafficProcessInit.py
    # portsTrafficProcessInit_HSS_HW.py
    # ZTEstaticsFetch222_read_database.py
    # ZTEstaticsFetch222.py
    # ZTEstaticsFetch1020.py
    # VoLTE_konghao.py
    # NFV_Indicator.py
    # BOSSSupervisionProcessInit.py
    # EPCERstasticFetch.py
# ) do (
    # set title=%%i
    # set pyname=%%i.py
    # REM start /b /wait TASKKILL /F /IM  !title!.exe /T
    # copy "C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe" "%path%\!title!.exe"
    # REM start cmd /c  "title !title!&%path%\!title!.exe !pyname!"
    # REM echo start: %%i
# )


# for %%i in (
    # D:\test\jiangyi\PDM\stasticsGet\DRAstaticFetch.py
    # D:\test\jiangyi\PDM\stasticsGet\EPCHWstasticFetch.py
    # D:\test\jiangyi\PDM\stasticsGet\ERMSCStasticFetch.py
    # D:\test\jiangyi\PDM\stasticsGet\gongdanStatic.py
    # D:\test\jiangyi\PDM\stasticsGet\HSSstaticsFetch.py
    # D:\test\jiangyi\PDM\stasticsGet\HWGMSCstasticFetch.py
    # D:\test\jiangyi\PDM\stasticsGet\HWMSCStasticFetch.py
    # D:\test\jiangyi\PDM\backendProcess\backendProcessInit.py
    # D:\test\jiangyi\PDM\backendProcess\portsTrafficProcessInit.py
    # D:\test\jiangyi\PDM\backendProcess\portsTrafficProcessInit_HSS_HW.py
    # D:\test\jiangyi\PDM\ZTEstatics\ZTEstaticsFetch222_read_database.py
    # D:\test\jiangyi\PDM\ZTEstatics\ZTEstaticsFetch222.py
    # D:\test\jiangyi\PDM\ZTEstatics\ZTEstaticsFetch1020.py
    # D:\test\jiangyi\PDM\backendProcess\VoLTE_konghao.py
    # D:\test\jiangyi\PDM\backendProcess\NFV_Indicator.py
    # D:\test\jiangyi\PDM\backendProcess\BOSSSupervisionProcessInit.py
    # D:\test\jiangyi\PDM\stasticsGet\EPCERstasticFetch.py
# ) do (
    # set title=%%i
    # set pyname=%%i.py
    # start /b /wait TASKKILL /F /IM  !title!.exe /T
    # start cmd /c  "title !title!&%path%\!title!.exe !pyname!"
    # REM echo start: %%i
# )


import os
import  psutil
import time
path = os.getcwd()
path = os.path.join(path,'EXE')
os.system(f"title {__file__}-PID:{os.getpid()}")

processes = [
    r'D:\test\jiangyi\PDM\stasticsGet\DRAstaticFetch.py',
    r'D:\test\jiangyi\PDM\stasticsGet\EPCHWstasticFetch.py',
    r'D:\test\jiangyi\PDM\stasticsGet\ERMSCStasticFetch.py',
    r'D:\test\jiangyi\PDM\stasticsGet\gongdanStatic.py',
    r'D:\test\jiangyi\PDM\stasticsGet\HSSstaticsFetch.py',
    r'D:\test\jiangyi\PDM\stasticsGet\HWGMSCstasticFetch.py',
    r'D:\test\jiangyi\PDM\stasticsGet\HWMSCStasticFetch.py',
    r'D:\test\jiangyi\PDM\backendProcess\backendProcessInit.py',
    r'D:\test\jiangyi\PDM\backendProcess\portsTrafficProcessInit.py',
    r'D:\test\jiangyi\PDM\backendProcess\portsTrafficProcessInit_HSS_HW.py',
    r'D:\test\jiangyi\PDM\ZTEstatics\ZTEstaticsFetch222_read_database.py',
    r'D:\test\jiangyi\PDM\ZTEstatics\ZTEstaticsFetch222.py',
    r'D:\test\jiangyi\PDM\ZTEstatics\ZTEstaticsFetch1020.py',
    r'D:\test\jiangyi\PDM\backendProcess\VoLTE_konghao.py',
    r'D:\test\jiangyi\PDM\backendProcess\NFV_Indicator.py',
    r'D:\test\jiangyi\PDM\backendProcess\BOSSSupervisionProcessInit.py',
    r'D:\test\jiangyi\PDM\stasticsGet\EPCERstasticFetch.py',
]

class mylog():
    def __init__(self,log_file=r"D:\work\debug.log",log_max_byte=150*1024*1024,log_backup_count=5):
        self.logger = None
        self.log_file = log_file
        self.log_max_byte = log_max_byte
        self.log_backup_count = log_backup_count
    
    def getLogger(self):
        if self.logger is not None:
            return self.logger
        self.logger = logging.getLogger()
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


def startProcesses():
    for i in processes:
        pyname = i.split('\\')[-1]
        title = pyname[:-3]
        KILLCMD = f"start /b /wait TASKKILL /F /IM  {title}.exe /T"
        os.system(KILLCMD)
        CPCMD = f'copy "C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37\\python.exe" "{path}\\{title}.exe"'
        os.system(CPCMD)
        STARTCMD = f'start cmd /c "title {title}&{path}\\{title}.exe {i}"'
        os.chdir(r'D:\test\jiangyi\PDM\stasticsGet')
        os.system(STARTCMD)


not_in_statics_pid = os.getpid()

def get_name_pid():
    pl = []
    for proc in psutil.process_iter():
        # if "python" in proc.name() and proc.pid != not_in_statics_pid:
            # print("[pid]: %d    [进程名]: %s" % (proc.pid,proc.name()))
        pl.append(proc.name())
    return pl

def check_pid(processes):
    myProcesses = [i.split("\\")[-1][:-2]+"exe" for i in processes]
    pl = get_name_pid()
    for i in myProcesses:
        if i not in pl:
            logging.warning(f'[ {i} ] should be restart at now !!!')
            p = processes[myProcesses.index(i)]
            os.system(f'start cmd /c "title {i[:-3]}&{path}\\{i} {p}"')
            


if __name__ == "__main__":
    import logging
    import logging.handlers
    import traceback
    mylog(log_file=r"./EXE/startProcesses.log").getLogger()
    try:
        startProcesses()
        
        while True:
            time.sleep(10)
            check_pid(processes)
    except:
        logging.error(traceback.format_exc())
        

















