import os,HTMLTestRunner,unittest,time

def create_suite():
    TestSuite = unittest.TestSuite()#测试集
    test_dir = os.getcwd()+'\\test_case\\'

    discover = unittest.defaultTestLoader.discover(
        start_dir=test_dir,
        pattern='Dent*.py',
        top_level_dir=None
    )

    # print (discover)

    for test_case  in discover:
        TestSuite.addTests(test_case)
    return TestSuite

now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = os.getcwd()+'\\report\\'+str(now)+'_result.html'
fp = open(report_name,'wb')

Runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='测试报告',
        description='测试用例执行情况'
    )

if __name__ == '__main__':
    TestSuite = create_suite()
    Runner.run(TestSuite)
    fp.close()