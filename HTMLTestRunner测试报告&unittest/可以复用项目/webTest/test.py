# -*- coding:utf-8 -*-

import requests
import unittest
import json
import HTMLTestRunner

class GetRequestTest(unittest.TestCase):

    def setUp(self):
        self.base_url="http://www.kuaidi100.com/"

    def tearDown(self):
        pass

    def test_login(self):
        self.data={"type":"yuantong","postid":"200528056708"}
        print("test_login@@@@@@")
        r=requests.post(self.base_url+"/query",self.data)
        dicts=json.loads(r.text)
        print(dicts)
        code=r.status_code
        print(code)

        self.assertEqual(code,200)
        self.assertEqual(dicts['status'],'200')

if __name__=="__main__":
    print("1")
    suite=unittest.TestSuite()
    suite.addTest(GetRequestTest("test_login"))
    fp=open(r'C:\Users\Mir-Z\Desktop\my\webTest\test.html','wb')
    #测试报告的标题与描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='测试报告的标题:',description='测试报告的描述:')
    runner.run(suite)
    fp.close()




