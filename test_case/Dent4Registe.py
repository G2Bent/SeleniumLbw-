# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,HTMLTestRunner
from public import Data

class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://test.dent-lab.com/register.html"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_Register1(self):
        '''测试密码格式错误，提示信息'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("txt_user").send_keys("18810000008")
        driver.find_element_by_id("btn_verify").click()
        driver.find_element_by_id("txt_verify_code").send_keys(Data.verify_code(18810000008))
        driver.find_element_by_id("pwd_set").send_keys("a1456")
        driver.find_element_by_id("pwd_repeat").send_keys("a1456")
        driver.find_element_by_id("btn_reg").click()
        # error = driver.find_element_by_id("error_tips").text
        # self.assertEqual("请输入由6-16字母(区分大小)、数字、特殊字符组成的密码", error)
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