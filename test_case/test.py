# import os
# caselist = os.listdir("test_case")
# # print(caselist)
# for a  in caselist:
#     s= a.split('.')[1:][0]
#     print(s)
#     if s =='py':
#         os.system('E:\\德雅项目文档\\测试脚本\\test\\test.txt')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re,HTMLTestRunner,os

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationError = []
        self.accept_next_alert = True

    #百度搜索用例
    def test_baidu_search1(self):
        '''测试找不到元素'''
        driver = self.driver
        driver.get(self.base_url+'/')
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        try:
            driver.find_element_by_id("kwddd").send_keys("selenium")
        except:
            driver.get_screenshot_as_file("TestScreenshot\%s.png"%now)

        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()
    #百度搜索用例
    def test_baidu_search2(self):
        '''测试正常找到元素'''
        driver = self.driver
        driver.get(self.base_url+'/')
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        try:
            driver.find_element_by_id("kw").send_keys("selenium")
        except:
            driver.get_screenshot_as_file("%s.png"%now)

        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationError)

    def suite(self):
        suite = unittest.TestSuite()
        for i in range(1,2):
            suite.addTest(Baidu("test_baidu_search%s"%str(i)))
        # suite.addTest(Baidu("test_baidu_search1"))
        return suite

if __name__=="__main__":
    unittest.main(defaultTest='suite')
