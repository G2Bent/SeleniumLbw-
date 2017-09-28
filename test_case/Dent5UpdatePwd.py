# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,HTMLTestRunner,os
from public import Data

class UpdatePwdTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://test.dent-lab.com/login.html"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_UpdatePwd1(self):
        '''修改用户密码'''
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        phone = "18800000000"
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("txt_user").send_keys(phone)
        driver.find_element_by_id("pwd_login").send_keys("a12345566")
        driver.find_element_by_id("btn_login").click()
        time.sleep(5)
        #点击修改密码按钮
        driver.find_element_by_xpath('//*[@id="btn_edit_pwd"]').click()
        driver.find_element_by_xpath('//*[@id="txt_old_pwd"]').send_keys("a12345566")
        driver.find_element_by_xpath('//*[@id="txt_new_pwd"]').send_keys("a123456")
        driver.find_element_by_xpath('//*[@id="txt_repeat_pwd"]').send_keys("a123456")
        driver.find_element_by_xpath('//*[@id="btn_save_pwd"]').click()
        driver.get_screenshot_as_file("TestScreenshot\%s.png" % now)
        time.sleep(5)

    def test_UpdatePwd2(self):
        '''输入密码不一致'''
        phone = "18800000000"
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("txt_user").send_keys(phone)
        driver.find_element_by_id("pwd_login").send_keys("a123456")
        driver.find_element_by_id("btn_login").click()
        time.sleep(5)
        #点击修改密码按钮
        driver.find_element_by_xpath('//*[@id="btn_edit_pwd"]').click()
        driver.find_element_by_xpath('//*[@id="txt_old_pwd"]').send_keys("a123456")
        driver.find_element_by_xpath('//*[@id="txt_new_pwd"]').send_keys("a123456")
        driver.find_element_by_xpath('//*[@id="txt_repeat_pwd"]').send_keys("a12345678")
        driver.find_element_by_xpath('//*[@id="btn_save_pwd"]').click()
        driver.get_screenshot_as_file("Image\输入密码不一致.png" )
        time.sleep(5)

    def test_UpdatePwd3(self):
        '''空密码提示'''
        phone = "18800000000"
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("txt_user").send_keys(phone)
        driver.find_element_by_id("pwd_login").send_keys("a123456")
        driver.find_element_by_id("btn_login").click()
        time.sleep(5)
        #点击修改密码按钮
        driver.find_element_by_xpath('//*[@id="btn_edit_pwd"]').click()
        driver.find_element_by_xpath('//*[@id="btn_save_pwd"]').click()
        time.sleep(5)

    def test_UpdatePwd4(self):
        '''输入格式不正确的密码'''
        phone = "18800000000"
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("txt_user").send_keys(phone)
        driver.find_element_by_id("pwd_login").send_keys("a123456")
        driver.find_element_by_id("btn_login").click()
        time.sleep(5)
        #点击修改密码按钮
        driver.find_element_by_xpath('//*[@id="btn_edit_pwd"]').click()
        driver.find_element_by_xpath('//*[@id="txt_old_pwd"]').send_keys("a123456")
        driver.find_element_by_xpath('//*[@id="txt_new_pwd"]').send_keys("a")
        driver.find_element_by_xpath('//*[@id="txt_repeat_pwd"]').send_keys("a")
        driver.find_element_by_xpath('//*[@id="btn_save_pwd"]').click()
        time.sleep(5)

    def test_UpdatePwd5(self):
        '''输入错误的原密码'''
        now = time.strftime("%Y%m%d%H%M%S")
        phone = "18800000000"
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("txt_user").send_keys(phone)
        driver.find_element_by_id("pwd_login").send_keys("a123456")
        driver.find_element_by_id("btn_login").click()
        time.sleep(5)
        #点击修改密码按钮
        driver.find_element_by_xpath('//*[@id="btn_edit_pwd"]').click()
        driver.find_element_by_xpath('//*[@id="txt_old_pwd"]').send_keys("a1234567887")
        driver.find_element_by_xpath('//*[@id="txt_new_pwd"]').send_keys("a1234565")
        driver.find_element_by_xpath('//*[@id="txt_repeat_pwd"]').send_keys("a1234565")
        driver.find_element_by_xpath('//*[@id="btn_save_pwd"]').click()
        driver.get_screenshot_as_file("..\Image\%s原密码错误.png"%now)
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
        img_path = r'..\image\修改密码\\' + now + '.png'
        driver.save_screenshot(img_path)
        time.sleep(2)
        driver.quit()
        self.assertEqual([], self.verificationErrors)

    # def suite(self):
    #     suite = unittest.TestSuite()
    #     for i in range(1,6):
    #         suite.addTest(UpdatePwdTest("test_UpdatePwd%s"%str(i)))
    #     return suite

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    # 将测试用例加入到测试容器中
    for i in range(1, 6):
        testunit.addTest(UpdatePwdTest("test_UpdatePwd%s"%str(i)))
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = r'..\report\\' + str(now) + '_result.html'
    fp = open(report_name, 'wb')
    Runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='修改密码测试报告',
        description='测试用例执行情况'
    )
    Runner.run(testunit)
    fp.close()