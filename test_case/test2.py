from selenium import webdriver
import unittest
import time,sys
import HTMLTestRunner,os


class BAIDU(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"

    def test_baidu_search(self):
        u'''什么都一样的啊'''
        driver = self.driver
        print("===============百度搜索1===============")
        driver.get(self.base_url+"/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("林你妹哦")
        driver.find_element_by_id("su").click()
        time.sleep(1)

    def tearDown(self):
        now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        img_path = '..\\report\\image\\'+str(now)+'.jpg'
        self.driver.get_screenshot_as_file(img_path)
        time.sleep(2)
        self.driver.quit()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(BAIDU("test_baidu_search"))
    return suite

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    HtmlFile = '..\\report\\'+str(now)+'report.html'
    Log =  '..\\report\\log\\' + str(now) + '.log'
    print(HtmlFile)
    fp = open(HtmlFile,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream = fp ,
                                           title = "这么吗",
                                           description = "用例执行情况")
    runner.run(suite())
    fp.close()