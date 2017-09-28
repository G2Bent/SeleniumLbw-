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

class FindPwdTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://test.dent-lab.com/login.html"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.name = "万能名"
        self.email = "944921374@qq.com"
        self.eremail = "000000000@qq.com"
        self.phone = "18814128583"
        self.phone1 = "18814100000"
        self.pwd = "a123456"
        self.errorphone ="188000"
        self.errorpwd = "aa"
        self.text = "我也不知道啊"

    def test_FindPwd1(self):
        '''手机号找回密码'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        #点击“忘记密码”
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="txt_user"]').send_keys("15812487685")
        driver.find_element_by_xpath('//*[@id="btn_verify"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="txt_verify_code"]').send_keys(Data.find_pwd("15812487685"))
        driver.find_element_by_xpath('//*[@id="txt_new_pwd"]').send_keys("a12345678")
        driver.find_element_by_xpath('//*[@id="txt_repeat_pwd"]').send_keys("a12345678")
        driver.find_element_by_xpath('//*[@id="btn_find_pwd"]').click()
        time.sleep(5)

    def test_FindPwd12(self):
        '''邮箱找回密码'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        #点击“忘记密码”
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="txt_user"]').send_keys(self.email)
        driver.find_element_by_xpath('//*[@id="btn_verify"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="txt_verify_code"]').send_keys(Data.find_pwd(self.email))
        driver.find_element_by_xpath('//*[@id="txt_new_pwd"]').send_keys("a12345678")
        driver.find_element_by_xpath('//*[@id="txt_repeat_pwd"]').send_keys("a12345678")
        driver.find_element_by_xpath('//*[@id="btn_find_pwd"]').click()
        time.sleep(5)

    def test_FindPwd2(self):
        '''未注册手机号'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        #点击“忘记密码”
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="txt_user"]').send_keys("13129087489")
        driver.find_element_by_xpath('//*[@id="btn_verify"]').click()
        time.sleep(5)

    def test_FindPwd13(self):
        '''未注册邮箱'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        #点击“忘记密码”
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="txt_user"]').send_keys(self.eremail)
        driver.find_element_by_xpath('//*[@id="btn_verify"]').click()
        time.sleep(5)

    def test_FindPwd3(self):
        '''手机号格式错误'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        #点击“忘记密码”
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="txt_user"]').send_keys("1550000000")
        driver.find_element_by_xpath('//*[@id="btn_verify"]').click()
        time.sleep(5)

    def test_FindPwd14(self):
        '''邮箱格式错误'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        #点击“忘记密码”
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="txt_user"]').send_keys("11@.com")
        driver.find_element_by_xpath('//*[@id="btn_verify"]').click()
        time.sleep(5)

    def test_FindPwd4(self):
        '''手机号/邮箱为空'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        #点击“忘记密码”
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="txt_user"]').send_keys()
        driver.find_element_by_xpath('//*[@id="btn_verify"]').click()

    def test_FindPwd5(self):
        '''验证码错误'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        #点击“忘记密码”
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="txt_user"]').send_keys(self.email)
        driver.find_element_by_xpath('//*[@id="btn_verify"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="txt_verify_code"]').send_keys("555555")
        driver.find_element_by_xpath('//*[@id="txt_new_pwd"]').send_keys("a12345678")
        driver.find_element_by_xpath('//*[@id="txt_repeat_pwd"]').send_keys("a12345678")
        driver.find_element_by_xpath('//*[@id="btn_find_pwd"]').click()
        time.sleep(5)

    def test_FindPwd6(self):
        '''验证码格式错误'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        #点击“忘记密码”
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="txt_user"]').send_keys("15812487685")
        driver.find_element_by_xpath('//*[@id="btn_verify"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="txt_verify_code"]').send_keys("555")
        driver.find_element_by_xpath('//*[@id="txt_new_pwd"]').send_keys("a12345678")
        driver.find_element_by_xpath('//*[@id="txt_repeat_pwd"]').send_keys("a12345678")
        driver.find_element_by_xpath('//*[@id="btn_find_pwd"]').click()
        time.sleep(5)

    def test_FindPwd7(self):
        '''直接输入验证码'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        #点击“忘记密码”
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="txt_user"]').send_keys(self.email)
        # driver.find_element_by_xpath('//*[@id="btn_verify"]').click()
        # time.sleep(5)
        driver.find_element_by_xpath('//*[@id="txt_verify_code"]').send_keys("543216")
        driver.find_element_by_xpath('//*[@id="txt_new_pwd"]').send_keys("a1234")
        driver.find_element_by_xpath('//*[@id="txt_repeat_pwd"]').send_keys("a1234")
        driver.find_element_by_xpath('//*[@id="btn_find_pwd"]').click()
        time.sleep(5)

    def test_FindPwd8(self):
        '''密码格式错误'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        #点击“忘记密码”
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="txt_user"]').send_keys(self.email)
        driver.find_element_by_xpath('//*[@id="btn_verify"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="txt_verify_code"]').send_keys(Data.find_pwd(self.email))
        driver.find_element_by_xpath('//*[@id="txt_new_pwd"]').send_keys("%%%%%%@@@")
        driver.find_element_by_xpath('//*[@id="txt_repeat_pwd"]').send_keys("%%%%%%@@@")
        driver.find_element_by_xpath('//*[@id="btn_find_pwd"]').click()
        time.sleep(5)

    def test_FindPwd9(self):
        '''密码长度错误'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        #点击“忘记密码”
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="txt_user"]').send_keys(self.email)
        driver.find_element_by_xpath('//*[@id="btn_verify"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="txt_verify_code"]').send_keys(Data.find_pwd(self.email))
        driver.find_element_by_xpath('//*[@id="txt_new_pwd"]').send_keys("a1234")
        driver.find_element_by_xpath('//*[@id="txt_repeat_pwd"]').send_keys("a1234")
        driver.find_element_by_xpath('//*[@id="btn_find_pwd"]').click()
        time.sleep(5)

    def test_FindPwd10(self):
        '''密码不一致'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        #点击“忘记密码”
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="txt_user"]').send_keys(self.email)
        driver.find_element_by_xpath('//*[@id="btn_verify"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="txt_verify_code"]').send_keys(Data.find_pwd(self.email))
        driver.find_element_by_xpath('//*[@id="txt_new_pwd"]').send_keys("a1234567")
        driver.find_element_by_xpath('//*[@id="txt_repeat_pwd"]').send_keys("a123456")
        driver.find_element_by_xpath('//*[@id="btn_find_pwd"]').click()
        time.sleep(5)

    def test_FindPwd11(self):
        '''文本框为空'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        #点击“忘记密码”
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="btn_find_pwd"]').click()
        time.sleep(5)

    def test_FindPwd15(self):
        '''跳过验证码，直接输入密码'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        #点击“忘记密码”
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/a[2]').click()
        driver.find_element_by_xpath('//*[@id="txt_user"]').send_keys(self.email)
        driver.find_element_by_xpath('//*[@id="txt_new_pwd"]').send_keys("a123456")
        driver.find_element_by_xpath('//*[@id="txt_repeat_pwd"]').send_keys("a123456")
        driver.find_element_by_xpath('//*[@id="btn_find_pwd"]').click()
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
        now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        img_path = r'..\image\忘记密码\\' + now+ '.png'
        driver.save_screenshot(img_path)
        time.sleep(2)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__=="__main__":
    testunit = unittest.TestSuite()
    #将测试用例加入到测试容器中
    for i in range(1,16):
        testunit.addTest(FindPwdTest("test_FindPwd%s" % str(i)))
    now = time.strftime("%Y-%m-%d-%H_%M_%S")
    report_name = r'..\report\\' + str(now) + '_result.html'
    fp = open(report_name, 'wb')
    Runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='找回密码测试报告',
        description='测试用例执行情况'
    )
    Runner.run(testunit)
    fp.close()
    # unittest.main(defaultTest='suite')
