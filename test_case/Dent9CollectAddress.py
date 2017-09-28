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

class CollectAddressTest(unittest.TestCase):
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

    def test_CllectAdd1(self):
        '''添加地址成功'''
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
        #点击添加新收货地址
        driver.find_element_by_xpath('//*[@id="btn_increase_address"]').click()
        driver.find_element_by_xpath('//*[@id="txt_username"]').send_keys(self.name)#输入用户名字
        driver.find_element_by_xpath('//*[@id="txt_mobile"]').send_keys(self.phone)#输入用户手机号码
        driver.find_element_by_xpath('//*[@id="add-province"]').click()#点击省
        driver.find_element_by_xpath('//*[@id="add-province"]/option[19]').click()#选择省
        driver.find_element_by_xpath('//*[@id="add-city"]').click()#点击市
        driver.find_element_by_xpath('//*[@id="add-city"]/option[1]').click()#选择市
        driver.find_element_by_xpath('//*[@id="add-district"]').click()#点击区
        # ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="add-district"]/option[3]'))
        driver.find_element_by_xpath('//*[@id="add-district"]/option[3]').click()  # 选择区
        # print(driver.find_element_by_xpath('//*[@id="add-district"]/option[1]').text)
        driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[5]/textarea').clear()
        driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[5]/textarea').send_keys(self.text)#输入详细地址信息
        driver.find_element_by_xpath('//*[@id="cd_default"]').click()#勾选默认地址
        driver.find_element_by_xpath('//*[@id="btn_save_increase"]').click()#点击确认
        time.sleep(5)

    def test_CllectAdd2(self):
        '''名字格式不正确'''
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
        #点击添加新收货地址
        driver.find_element_by_xpath('//*[@id="btn_increase_address"]').click()
        driver.find_element_by_xpath('//*[@id="txt_username"]').send_keys('n')#输入用户名字
        driver.find_element_by_xpath('//*[@id="txt_mobile"]').send_keys(self.phone)#输入用户手机号码
        time.sleep(5)

    def test_CllectAdd3(self):
        '''手机号码不正确'''
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
        #点击添加新收货地址
        driver.find_element_by_xpath('//*[@id="btn_increase_address"]').click()
        driver.find_element_by_xpath('//*[@id="txt_username"]').send_keys(self.name)#输入用户名字
        driver.find_element_by_xpath('//*[@id="txt_mobile"]').send_keys(self.errorphone)#输入用户手机号码
        driver.find_element_by_xpath('//*[@id="add-province"]').click()#点击省
        time.sleep(5)

    def test_CllectAdd4(self):
        '''无点击提示信息'''
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
        #点击添加新收货地址
        driver.find_element_by_xpath('//*[@id="btn_increase_address"]').click()
        driver.find_element_by_xpath('//*[@id="btn_save_increase"]').click()#点击确认
        time.sleep(5)

    def test_CllectAdd6(self):
        '''不添加详细地址信息'''
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
        #点击添加新收货地址
        driver.find_element_by_xpath('//*[@id="btn_increase_address"]').click()
        driver.find_element_by_xpath('//*[@id="txt_username"]').send_keys(self.name)#输入用户名字
        driver.find_element_by_xpath('//*[@id="txt_mobile"]').send_keys(self.phone)#输入用户手机号码
        driver.find_element_by_xpath('//*[@id="add-province"]').click()#点击省
        driver.find_element_by_xpath('//*[@id="add-province"]/option[19]').click()#选择省
        driver.find_element_by_xpath('//*[@id="add-city"]').click()#点击市
        driver.find_element_by_xpath('//*[@id="add-city"]/option[1]').click()#选择市
        driver.find_element_by_xpath('//*[@id="add-district"]').click()#点击区
        driver.find_element_by_xpath('//*[@id="add-district"]/option[1]').click()#选择区
        driver.find_element_by_xpath('//*[@id="btn_save_increase"]').click()#点击确认
        time.sleep(5)

    def test_CllectAdd7(self):
        '''删除地址成功'''
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
        #点击删除收货地址(默认是第一个)
        driver.find_element_by_xpath('//*[@id="btn_delete_address"]').click()
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
        img_path = r'..\image\添加地址\\' + now + '.png'
        driver.save_screenshot(img_path)
        time.sleep(2)
        driver.quit()
        self.assertEqual([], self.verificationErrors)

    # def suite(self):
    #     suite = unittest.TestSuite()
    #     for i in range(1,6):
    #         suite.addTest(CollectAddressTest("test_CllectAdd%s"%str(i)))
    #     return suite

if __name__=="__main__":
    testunit = unittest.TestSuite()
    # 将测试用例加入到测试容器中
    for i in range(1, 8):
        testunit.addTest(CollectAddressTest("test_CllectAdd%s"%str(i)))
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = r'..\report\\' + str(now) + '_result.html'
    fp = open(report_name, 'wb')
    Runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='添加地址测试报告',
        description='测试用例执行情况'
    )
    Runner.run(testunit)
    fp.close()