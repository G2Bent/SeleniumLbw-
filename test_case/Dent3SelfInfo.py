from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,HTMLTestRunner,os
from public import Data

class SelfInfoTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://test.dent-lab.com/login.html"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_SelfInfo1(self):
        '''测试用户登录成功跳转到个人信息页面'''
        phone = "18800000000"
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("txt_user").send_keys(phone)
        driver.find_element_by_id("pwd_login").send_keys("a123456")
        driver.find_element_by_id("btn_login").click()
        time.sleep(5)

    def test_SelfInfo2(self):
        '''修改用户昵称'''
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
        driver.find_element_by_xpath('//*[@id="text-uname"]').send_keys("广州恒大")
        driver.find_element_by_xpath('//*[@id="btn_save"]').click()
        time.sleep(5)

    def test_SelfInfo3(self):
        '''测试昵称长度'''
        phone = "18800000000"
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("txt_user").send_keys(phone)
        driver.find_element_by_id("pwd_login").send_keys("a123456")
        driver.find_element_by_id("btn_login").click()
        time.sleep(5)
        # 点击编辑按钮
        driver.find_element_by_xpath('//*[@id="btn_edit"]').click()
        driver.find_element_by_xpath('//*[@id="text-uname"]').send_keys("广州恒大的点点滴滴多多多多多多多多多多多多多"
                                                                        "多多多多多多多多多多多多多多多多的点点滴滴多多"
                                                                        "多多多多多多多多多多多多多多的二二二二二二二二"
                                                                        "二二二二二无无无无无无无无")
        driver.find_element_by_xpath('//*[@id="btn_save"]').click()

        time.sleep(5)

    def test_SelfInfo4(self):
        '''修改用户性别'''
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
        driver.find_element_by_xpath('//*[@id="radio_male"]').click()#修改性别为男性
        driver.find_element_by_xpath('//*[@id="btn_save"]').click()
        time.sleep(5)

    def test_SelfInfo5(self):
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

    def test_SelfInfo6(self):
        '''上传头像成功'''
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
        driver.find_element_by_xpath('//*[@id="selectfiles1"]').click()
        os.system(os.path.dirname(os.getcwd())+'\Autolt\正常头像.exe')
        time.sleep(2)
        # s = driver.switch_to_alert()
        # s.accept()
        # time.sleep(3)
        # driver.find_element(By.XPATH("//*[@id='alert']/input")).click()
        driver.find_element_by_xpath('//*[@id="btn_save"]').click()
        s = driver.switch_to_alert()
        s.accept()
        time.sleep(3)

    def test_SelfInfo7(self):
        '''修改用户不能超过2M'''
        phone = "18800000000"
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("txt_user").send_keys(phone)
        driver.find_element_by_id("pwd_login").send_keys("a123456")
        driver.find_element_by_id("btn_login").click()
        time.sleep(5)
        # 点击编辑按钮
        driver.find_element_by_xpath('//*[@id="btn_edit"]').click()
        driver.find_element_by_xpath('//*[@id="selectfiles1"]').click()
        os.system(os.path.dirname(os.getcwd()) + '\Autolt\超出2M头像.exe')
        time.sleep(2)
        s = driver.switch_to_alert()
        s.accept()
        time.sleep(2)
        # driver.find_element(By.XPATH("//*[@id='alert']/input")).click()
        driver.find_element_by_xpath('//*[@id="btn_save"]').click()
        time.sleep(3)

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
        img_path = r'..\image\个人信息\\' + now + '.png'
        driver.save_screenshot(img_path)
        time.sleep(2)
        driver.quit()
        self.assertEqual([], self.verificationErrors)

    # def suite(self):
    #     suite = unittest.TestSuite()
    #     for i in range(1,8):
    #         suite.addTest(SelfInfoTest("test_SelfInfo%s"%str(i)))
    #     return suite
if __name__ == '__main__':
    testunit = unittest.TestSuite()
    # 将测试用例加入到测试容器中
    for i in range(1, 8):
        testunit.addTest(SelfInfoTest("test_SelfInfo%s"%str(i)))
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = r'..\report\\' + str(now) + '_result.html'
    fp = open(report_name, 'wb')
    Runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='个人信息测试报告',
        description='测试用例执行情况'
    )
    Runner.run(testunit)
    fp.close()