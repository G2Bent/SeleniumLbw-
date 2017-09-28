# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,HTMLTestRunner,os,random
from public import Data
from selenium.webdriver.common.action_chains import *

class CollectEditTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://test.dent-lab.com/login.html"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.name = "万能名"
        self.email = "944921374@qq.com"
        self.phone = "18814128583"
        self.phone1 = "18814100000"
        self.pwd = "a123456"
        self.errorphone ="188000"
        self.errorpwd = "aa"
        self.text = "我也不知道啊"

    def test_CllectEdit1(self):
        '''修改地址成功'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("txt_user").send_keys(self.email)
        driver.find_element_by_id("pwd_login").send_keys("a123456")
        driver.find_element_by_id("btn_login").click()
        time.sleep(10)
        # 点击收货地址菜单
        dr = driver.find_element_by_xpath('//*[@id="app"]/div[2]/ul/li[2]/a')
        ActionChains(driver).move_to_element(dr).perform()
        dr.click()
        time.sleep(3)
        #点击编辑地址
        driver.find_elements_by_xpath('//*[@id="btn_edit_address"]')[1].click()
        qq = driver.find_element_by_xpath('//*[@id="txt_edit_username"]')
        qq.send_keys(Keys.CONTROL+'a')
        driver.find_element_by_xpath('//*[@id="txt_edit_username"]').send_keys("修改")
        driver.find_element_by_xpath('//*[@id="txt_edit_mobile"]').clear()
        driver.find_element_by_xpath('//*[@id="txt_edit_mobile"]').send_keys(self.phone)
        driver.find_element_by_xpath('//*[@id="province"]').click()  # 点击省
        driver.find_element_by_xpath('//*[@id="province"]/option[19]').click()  # 选择省
        driver.find_element_by_xpath('//*[@id="city"]').click()  # 点击市
        driver.find_element_by_xpath('//*[@id="city"]/option[1]').click()  # 选择市
        driver.find_element_by_xpath('//*[@id="district"]').click()  # 点击区
        driver.find_element_by_xpath('//*[@id="district"]/option[4]').click()  # 选择区
        driver.find_element_by_xpath('//*[@id="txt_edit_detail"]').clear()
        driver.find_element_by_xpath('//*[@id="txt_edit_detail"]').send_keys(self.text)
        driver.find_element_by_xpath('//*[@id="cd_edit_default"]').click()#这点击不一定是选上的点击
        driver.find_element_by_xpath('//*[@id="btn_save_edit"]').click()#点击确认按钮

    def test_CllectEdit2(self):
        '''修改地址不做操作'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("txt_user").send_keys(self.email)
        driver.find_element_by_id("pwd_login").send_keys("a123456")
        driver.find_element_by_id("btn_login").click()
        time.sleep(5)
        # 点击收货地址菜单
        dr = driver.find_element_by_xpath('//*[@id="app"]/div[2]/ul/li[2]/a')
        ActionChains(driver).move_to_element(dr).perform()
        dr.click()
        time.sleep(3)
        #点击编辑地址
        driver.find_elements_by_xpath('//*[@id="btn_edit_address"]')[1].click()
        driver.find_element_by_xpath('//*[@id="btn_save_edit"]').click()#点击确认按钮

    def test_CllectEdit3(self):
        '''修改默认地址'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("txt_user").send_keys(self.email)
        driver.find_element_by_id("pwd_login").send_keys("a123456")
        driver.find_element_by_id("btn_login").click()
        time.sleep(10)
        # 点击收货地址菜单
        dr = driver.find_element_by_xpath('//*[@id="app"]/div[2]/ul/li[2]/a')
        ActionChains(driver).move_to_element(dr).perform()
        dr.click()
        time.sleep(3)
        #点击编辑地址
        driver.find_elements_by_xpath('//*[@id="btn_edit_address"]')[0].click()
        driver.find_element_by_xpath('//*[@id="cd_edit_default"]').click()#这点击是选上默认地址的
        driver.find_element_by_xpath('//*[@id="btn_save_edit"]').click()#点击确认按钮
        time.sleep(2)

    def test_CllectEdit4(self):
        '''修改默认地址'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("txt_user").send_keys(self.email)
        driver.find_element_by_id("pwd_login").send_keys("a123456")
        driver.find_element_by_id("btn_login").click()
        time.sleep(10)
        # 点击收货地址菜单
        dr = driver.find_element_by_xpath('//*[@id="app"]/div[2]/ul/li[2]/a')
        ActionChains(driver).move_to_element(dr).perform()
        dr.click()
        time.sleep(3)
        #点击编辑地址
        driver.find_elements_by_xpath('//*[@id="btn_default_address"]')[2].click()
        time.sleep(2)

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
        now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        img_path = r'..\image\编辑地址\\' + now+ '.png'
        driver.save_screenshot(img_path)
        time.sleep(2)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__=="__main__":
    testunit = unittest.TestSuite()
    #将测试用例加入到测试容器中
    for i in range(1, 5):
        testunit.addTest(CollectEditTest("test_CllectEdit%s" % str(i)))
    now = time.strftime("%Y-%m-%d%H_%M_%S")
    report_name = r'..\report\\' + str(now) + '_result.html'
    fp = open(report_name, 'wb')
    Runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='编辑收货地址测试报告',
        description='测试用例执行情况'
    )
    Runner.run(testunit)
    fp.close()
    # unittest.main(defaultTest='suite')
