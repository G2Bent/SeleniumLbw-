# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,HTMLTestRunner
from public import Data

class DentTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://test.dent-lab.com/login.html"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_Login1(self):
        '''测试登录和注册页面的链接是否正确'''
        phone = "1880000000"
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[3]/a").click()
        time.sleep(5)
        # driver.find_element_by_partial_link_text("没有账号").click()
        driver.find_element_by_partial_link_text("已有账号").click()
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
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
    unittest.main()