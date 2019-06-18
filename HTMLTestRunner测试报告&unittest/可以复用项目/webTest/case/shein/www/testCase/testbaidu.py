# -*- coding:utf-8 -*- 
import sys
sys.path.append(r"C:\Users\Mir-Z\Desktop\my\webTest")
from time import sleep
from selenium import webdriver
import unittest
from comm.Log import MyLog as Log

class Login(unittest.TestCase):
    case_name = "baidu_search"

    def setUp(self):
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.log.build_start_line(self.case_name)        
        
        self.driver = webdriver.Chrome()
        # 绐楀彛鏈�ぇ鍖�
        self.driver.maximize_window()
        self.msg = "大西瓜"
        self.url = 'http://www.baidu.com'

    def testSearch(self):
        """
        test body
        :return:
        """
        print("daxigua")
        self.logger.debug("daxigua")
        
        # open browser
        self.driver.get(self.url)
        sleep(3)
        # click search input
        self.driver.find_element_by_id('kw').click()
        sleep(1)

        # input value
        self.driver.find_element_by_id('kw').send_keys(self.msg)
        sleep(1)
        self.driver.find_element_by_id('su').click()
        sleep(1)

    def tearDown(self):
        self.driver.close()

#if __name__ == "__main__":
    #unittest.main()

