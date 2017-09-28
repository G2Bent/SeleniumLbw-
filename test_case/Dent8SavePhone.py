# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,HTMLTestRunner,os,random
from public import Data

class SavePhoneTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://test.dent-lab.com/login.html"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.email = "944921374@qq.com"
        self.phone = "18814128583"
        self.phone1 = "18814100000"
        self.pwd = "a123456"
        self.errorphone ="188000"
        self.errorpwd = "aa"

    def test_SavePhone1(self):
        '''绑定手机'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("txt_user").send_keys(self.email)
        driver.find_element_by_id("pwd_login").send_keys("a123456")
        driver.find_element_by_id("btn_login").click()
        time.sleep(5)
        # 点击绑定手机按钮
        driver.find_element_by_xpath('//*[@id="btn_edit_phone"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="txt_phone"]').send_keys("15000000000")
        driver.find_element_by_xpath('//*[@id="btn_phone_verify"]').click()
        driver.find_element_by_xpath('//*[@id="txt_phone_verify_code"]').send_keys(Data.email_code("15000000000"))
        driver.find_element_by_xpath('//*[@id="btn_save_phone"]').click()
        time.sleep(5)

    def test_SavePhone2(self):
        '''输入错误手机号码'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("txt_user").send_keys(self.email)
        driver.find_element_by_id("pwd_login").send_keys("a123456")
        driver.find_element_by_id("btn_login").click()
        time.sleep(5)
        #点击绑定手机按钮
        driver.find_element_by_xpath('//*[@id="btn_edit_phone"]').click()
        driver.find_element_by_xpath('//*[@id="txt_phone"]').send_keys(self.errorphone)
        driver.find_element_by_xpath('//*[@id="btn_phone_verify"]').click()
        time.sleep(5)

    def test_SavePhone3(self):
        '''输入已经绑定的手机号码'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("txt_user").send_keys(self.email)
        driver.find_element_by_id("pwd_login").send_keys("a123456")
        driver.find_element_by_id("btn_login").click()
        time.sleep(5)
        # 点击绑定手机按钮
        driver.find_element_by_xpath('//*[@id="btn_edit_phone"]').click()
        driver.find_element_by_xpath('//*[@id="txt_phone"]').send_keys(self.phone)
        driver.find_element_by_xpath('//*[@id="btn_phone_verify"]').click()
        # driver.find_element_by_xpath('//*[@id="txt_verify_code"]').send_keys(Data.email_code("944921374@qq.com"))
        # driver.find_element_by_xpath('//*[@id="btn_save_email"]').click()
        time.sleep(5)

    def test_SavePhone4(self):
        '''输入错误验证码'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("txt_user").send_keys(self.email)
        driver.find_element_by_id("pwd_login").send_keys("a123456")
        driver.find_element_by_id("btn_login").click()
        time.sleep(5)
        # 点击绑定手机按钮
        driver.find_element_by_xpath('//*[@id="btn_edit_phone"]').click()
        driver.find_element_by_xpath('//*[@id="txt_phone"]').send_keys(self.phone1)
        driver.find_element_by_xpath('//*[@id="btn_phone_verify"]').click()
        driver.find_element_by_xpath('//*[@id="txt_phone_verify_code"]').send_keys("12345")
        driver.find_element_by_xpath('//*[@id="btn_save_phone"]').click()
        time.sleep(5)

    def test_SavePhone5(self):
        '''绑定空号码'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("txt_user").send_keys(self.email)
        driver.find_element_by_id("pwd_login").send_keys("a123456")
        driver.find_element_by_id("btn_login").click()
        time.sleep(5)
        # 点击绑定手机按钮
        driver.find_element_by_xpath('//*[@id="btn_edit_phone"]').click()
        driver.find_element_by_xpath('//*[@id="btn_save_phone"]').click()
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
        img_path = r'..\image\绑定手机\\' + now + '.png'
        driver.save_screenshot(img_path)
        time.sleep(2)
        driver.quit()
        self.assertEqual([], self.verificationErrors)

    # def suite(self):
    #     suite = unittest.TestSuite()
    #     for i in range(1,6):
    #         suite.addTest(SavePhoneTest("test_SavePhone%s"%str(i)))
    #     return suite

if __name__=="__main__":
    testunit = unittest.TestSuite()
    # 将测试用例加入到测试容器中
    for i in range(1, 6):
        testunit.addTest(SavePhoneTest("test_SavePhone%s"%str(i)))
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = r'..\report\\' + str(now) + '_result.html'
    fp = open(report_name, 'wb')
    Runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='绑定手机测试报告',
        description='测试用例执行情况'
    )
    Runner.run(testunit)
    fp.close()
