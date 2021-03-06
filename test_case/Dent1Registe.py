# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,HTMLTestRunner,os
from public import Data

class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://test.dent-lab.com/login.html"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.phone= "18814128583"

    def test_Register1(self):
        '''测试用户注册成功'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/a[1]').click()
        driver.find_element_by_id("txt_user").send_keys(self.phone)
        driver.find_element_by_id("btn_verify").click()
        driver.find_element_by_id("txt_verify_code").send_keys(Data.verify_code(self.phone))
        driver.find_element_by_id("pwd_set").send_keys("a123456")
        driver.find_element_by_id("pwd_repeat").send_keys("a123456")
        driver.find_element_by_id("btn_reg").click()
        time.sleep(5)

    def test_Register2(self):
        '''测试手机号码错误，提示错误信息'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/a[1]').click()
        driver.find_element_by_id("txt_user").send_keys("188141283")
        driver.find_element_by_id("btn_reg").click()
        error = driver.find_element_by_id("error_tips").text
        self.assertEqual("手机号或密码不能为空",error)
        print(error)
        time.sleep(5)

    def test_Register3(self):
        '''测试输入错误验证码，提示信息'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/a[1]').click()
        driver.find_element_by_id("txt_user").send_keys("15500000000")
        driver.find_element_by_id("btn_verify").click()
        driver.find_element_by_id("txt_verify_code").send_keys("111111")
        driver.find_element_by_id("pwd_set").send_keys("a123456")
        driver.find_element_by_id("pwd_repeat").send_keys("a123456")
        driver.find_element_by_id("btn_reg").click()
        # error = driver.find_element_by_id("error_tips").text
        # self.assertEqual("验证码错误", error)
        time.sleep(5)

    def test_Register4(self):
        '''测试密码格式错误，提示信息'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/a[1]').click()
        driver.find_element_by_id("txt_user").send_keys("15500000000")
        driver.find_element_by_id("btn_verify").click()
        driver.find_element_by_id("txt_verify_code").send_keys(Data.verify_code("15500000000"))
        driver.find_element_by_id("pwd_set").send_keys("a1456")
        driver.find_element_by_id("pwd_repeat").send_keys("a1456")
        driver.find_element_by_id("btn_reg").click()
        # error = driver.find_element_by_id("error_tips").text
        # self.assertEqual("请输入由6-16字母(区分大小)、数字、特殊字符组成的密码", error)
        time.sleep(5)

    def test_Register5(self):
        '''测试输入密码不一致，提示信息'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        #//*[@id="app"]/div/div[2]/div[3]/a[1]     注册xpath
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/a[1]').click()
        driver.find_element_by_id("txt_user").send_keys("18800000000")
        driver.find_element_by_id("btn_verify").click()
        driver.find_element_by_id("txt_verify_code").send_keys(Data.verify_code(18800000000))
        driver.find_element_by_id("pwd_set").send_keys("a12345678")
        driver.find_element_by_id("pwd_repeat").send_keys("a12344")
        driver.find_element_by_id("btn_reg").click()
        # error = driver.find_element_by_id("error_tips").text
        # self.assertEqual("密码不一致", error)
        time.sleep(5)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        driver = self.driver
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        img_path = r'..\image\手机注册\\' + now + '.png'
        driver.save_screenshot(img_path)
        time.sleep(2)
        driver.quit()
        self.assertEqual([], self.verificationErrors)
    # def suite(self):
    #     suite = unittest.TestSuite()
    #     for i in range(1,6):
    #         suite.addTest(RegisterTest("test_Register%s"%str(i)))
    #     return suite

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    # 将测试用例加入到测试容器中
    for i in range(1, 6):
        testunit.addTest(RegisterTest("test_Register%s" % str(i)))
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = r'..\report\\' + str(now) + '_result.html'
    fp = open(report_name, 'wb')
    Runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='手机注册测试报告',
        description='测试用例执行情况'
    )
    Runner.run(testunit)
    fp.close()