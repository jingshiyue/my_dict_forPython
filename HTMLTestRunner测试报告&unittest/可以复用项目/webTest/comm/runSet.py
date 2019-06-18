import os
import sys
import unittest
sys.path.append("..")
import readConfig as readConfig
from comm.Log import MyLog as Log
from comm.webDriver import MyDriver as Driver

log = Log.get_log()
logger = log.get_logger()
driver = Driver.get_browser()
filePath = ''


def set_case_list():
    """
    read case name from 'caseList.txt'
    :return:
    """
    caseList = []
    caseListPath = os.path.join(readConfig.proDir, "caseList.txt")
    fb = open(caseListPath)
    for case in fb.readlines():
        data = str(case)
        if data != "" and not data.startswith("#"):
            caseList.append(data.replace("\n", ""))
    fb.close()
    return caseList


def set_suite():
    """
    set test suite
    :return:
    """
    global filePath
    suite_list = unittest.TestSuite()
    suite_module = []                  

    case_list = set_case_list()  #case_list ['shein/www/testLogin', 'shein/www/testRegister', 'romwe/es/testLogin']
    logger.debug(case_list)
    for case in case_list:
        name = str(case).split("/")[-1]
        webname = str(case).split("/")[0]
        sitename = str(case).split("/")[1]

        filePath = os.path.join(readConfig.proDir, "case", webname, sitename, "testCase")
        # filePath = os.path.join(readConfig.proDir, "testCase")
        logger.debug(name)  #testLogin
        logger.debug(filePath) #C:\Users\Mir-Z\Desktop\my\webTest\case\romwe\es\testCase
        discover = unittest.defaultTestLoader.discover(filePath, pattern=name+'.py', top_level_dir=None)
        logger.debug(type(discover))  #<class 'unittest.suite.TestSuite'>
        logger.debug((discover))  #<unittest.suite.TestSuite tests=[<unittest.suite.TestSuite tests=[<unittest.loader._FailedTest testMethod=testLogin>]>]>
        suite_module.append(discover)       


    if len(suite_module) > 0:
        for case in suite_module:
            for name in case:
                suite_list.addTest(name)
                logger.debug(suite_list)
    else:
        return None
    logger.debug(suite_list)
    return suite_list

set_suite()


def set_website():
    """
    Set website by name
    :return:
    """
    name_list = set_case_list()
    for case in name_list:
        data = str(case)
        if data != "" and not data.startswith("#"):
            web = data.split("/")[0]
            site = data.split("/")[1]
            name = web.upper()
            break
    driver.open_browser(name, site)


def close_browser():
    """
    quite browser
    :return:
    """
    driver.close_browser()


def get_web():
    """
    get web
    :return: web
    """
    name_list = set_case_list()
    for case in name_list:
        data = str(case)
        if data != "" and not data.startswith("#"):
            web = data.split("/")[0]
            break
    return web


def get_site():
    """
    get site
    :return:site
    """
    name_list = set_case_list()
    for case in name_list:
        data = str(case)
        if data != "" and not data.startswith("#"):
            site = data.split("/")[1]
            break
    return site

