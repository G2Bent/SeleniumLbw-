from selenium import webdriver
import unittest
import time,sys
import HTMLTestRunner,os


class BAIDU(unittest.TestCase):
    '''这是百度测试网页，里面带有截图功能'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"
    def test_baidu_search(self):
        driver = self.driver
        print("===============百度搜索1===============")
        driver.get(self.base_url+"/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("林你妹哦")
        # driver.find_element_by_id("su").click()
        time.sleep(3)

    def screenshort(self):
        now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        # 必须要打印路径HTMLTestRunner才能捕获并且生成路径，\image\**.png 是获取路径的条件，必须这样的目录
        # img_path = 'E:\\Test_png\\'+now+'.png'
        img_path = 'screenshort\\' + now + '.png'
        self.driver.get_screenshot_as_file(img_path)

    def tearDown(self):
        # driver = self.driver
        # now = time.strftime("%Y%m%d", time.localtime(time.time()))
        # # 必须要打印路径HTMLTestRunner才能捕获并且生成路径，\image\**.png 是获取路径的条件，必须这样的目录
        # # img_path = 'E:\\Test_png\\'+now+'.png'
        # img_path = os.getcwd() + '\\image\\' + str(now) + '.jpg'
        # # print(img_path)
        # driver.save_screenshot(img_path)
        time.sleep(2)
        self.driver.quit()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(BAIDU("test_baidu_search"))

    return suite

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    HtmlFile = os.getcwd()+'\\report\\'+str(now)+'report.html'
    print(HtmlFile)
    fp = open(HtmlFile,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream = fp ,
                                           title = "这么吗",
                                           description = "用例执行情况")
    runner.run(suite())
    fp.close()