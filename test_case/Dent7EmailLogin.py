# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,HTMLTestRunner,os
from public import Data

class EmailLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://test.dent-lab.com/login.html"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_EmailLogin1(self):
        '''测试用户登录成功'''
        email = "83838@sina.com"
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("txt_user").send_keys(email)
        driver.find_element_by_id("pwd_login").send_keys("a12345678")
        driver.find_element_by_id("btn_login").click()
        time.sleep(5)

    def test_EmailLogin2(self):
        '''测试用户名或密码错误'''
        email = "1880000000.com"
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("txt_user").send_keys(email)
        driver.find_element_by_id("pwd_login").send_keys("a12346")
        driver.find_element_by_id("btn_login").click()
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
        img_path = os.getcwd() + '\\image\\' + str(now) + '.png'
        driver.save_screenshot(img_path)
        time.sleep(2)
        driver.quit()
        self.assertEqual([], self.verificationErrors)

    def suite(self):
        suite = unittest.TestSuite()
        for i in range(1,3):
            suite.addTest(EmailLoginTest("test_UpdatePwd%s"%str(i)))
        return suite
if __name__ == '__main__':
    unittest.main()