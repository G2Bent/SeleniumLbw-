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
        '''修改用户出生日期'''
        phone = "18800000000"
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("txt_user").send_keys(phone)
        driver.find_element_by_id("pwd_login").send_keys("a123456")
        driver.find_element_by_id("btn_login").click()
        time.sleep(5)
        #点击编辑按钮
        driver.find_element_by_xpath('//*[@id="btn_edit"]').click()
        driver.find_element_by_xpath('//*[@id="app"]/div[4]/div[3]/div[3]/select[1]').click()#点击年
        driver.find_element_by_xpath('//*[@id="app"]/div[4]/div[3]/div[3]/select[1]/option[6]').click()#选择年
        driver.find_element_by_xpath('//*[@id="app"]/div[4]/div[3]/div[3]/select[2]').click()#点击月
        driver.find_element_by_xpath('//*[@id="app"]/div[4]/div[3]/div[3]/select[2]/option[4]').click()#选择月
        driver.find_element_by_xpath('//*[@id="app"]/div[4]/div[3]/div[3]/select[3]').click()#点击日
        driver.find_element_by_xpath('//*[@id="app"]/div[4]/div[3]/div[3]/select[3]/option[9]').click()#选择日
        driver.find_element_by_xpath('//*[@id="btn_save"]').click()
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