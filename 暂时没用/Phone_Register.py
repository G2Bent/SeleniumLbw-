# coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from usedata import get_webinfo,XlUserinfo
from log_module import Loginfo, Xlloginfo


def get_ele_times(driver, times, func):
    return WebDriverWait(driver, times).until(func)

#加载驱动，打开浏览器方法
def openBrower():
    '''
    return webdriver Handle
    返回一个驱动，用来打开浏览器
    '''
    webdriver_handle = webdriver.Firefox()
    return webdriver_handle

#输入链接URL方法
def openUrl(handle, url):
    '''
    load url
    打开我们需要的URL，并且最大化浏览器
    '''
    handle.get(url)
    handle.maximize_window()

#查找注册定位元素
def findRegisterElement(d,arg):
    '''
    字典中需要的元素：
    1:btnreg
    2:userid
    3:phoneid
    4:verifyid
    5:InVerifyid
    6:pwdid
    7:setpwdid
    8:registerid
    '''
  # if 'text_id' in arg:
    #     ele_login = get_ele_times(d, 10, lambda d: d.find_element_by_link_text(arg['text_id']))
    #     ele_login.click()
    btnReg = d.find_element_by_id(arg['btnreg'])#查找注册按钮
    userID = d.find_element_by_id(arg['userid'])#查找用户昵称元素
    phoneEle = d.find_element_by_id(arg['phoneid'])#查找注册手机号文本框
    verifyEle = d.find_element_by_id(arg['verifyid'])#查找验证码按钮元素
    inVerifyEle = d.find_element_by_id(arg['InVerifyid'])#查找输入验证码文本框
    pwdEle = d.find_element_by_id(arg['pwdid'])#查找注册密码文本框
    setpwdEle = d.find_element_by_id(arg['setpwdid'])#查找确认密码文本框
    loginEle = d.find_element_by_id(arg['registerid'])#查找点击注册的按钮
    return btnReg,userID,phoneEle,verifyEle,inVerifyEle,pwdEle,setpwdEle,loginEle

#输入的值
def sendVals(eletuple, arg):
    '''
    ele tuple
    account : uname, pwd
    '''
    listkey = ['phone', 'verify','pwd','setpwd']
    i = 0
    for key in listkey:
        eletuple[i].send_keys('')
        eletuple[i].clear()
        eletuple[i].send_keys(arg[key])
        i += 1
    eletuple[1].click()
    eletuple[4].click()

#测试报告
def checkResult(d, err_id, arg, log):
    result = False
    time.sleep(2)
    try:
        err = d.find_element_by_id(err_id)
        print("注册失败!")
        # msg = 'uname=%s pwd=%s:error:%s\n'%(arg['uname'],arg['pwd'], err.text)
        log.log_write(arg['phone'], arg['verify'], arg['pwd'],arg['setpwd'], 'Error', err.text)

    except:
        print("注册成功!")
        msg = 'uname=%s pwd=%s:pass\n' % (arg['uname'], arg['pwd'])
        # log.log_write(msg)
        log.log_write(arg['phone'], arg['verify'], arg['pwd'], arg['setpwd'], 'Pass')
        result = True
    return result

#退出登录
def logout(d, ele_dict):
    # d.find_element_by_class_name(ele_dict['usermenu']).click()
    d.find_element_by_link_text(ele_dict['logout']).click()

#注册测试
def register_test(ele_dict, user_list):
    d = openBrower()
    # log = Loginfo()
    log = Xlloginfo()
    log.log_init('sheet1', 'phone', 'verify', 'pwd','setpwd' ,'msg')
    openUrl(d, ele_dict['url'])
    ele_tuple = findRegisterElement(d, ele_dict)
    for arg in user_list:
        sendVals(ele_tuple, arg)
        result = checkResult(d, ele_dict['errorid'], arg, log)
        if result:
            # logout
            logout(d, ele_dict)
            # register
            ele_tuple = findRegisterElement(d, ele_dict)
    log.log_close()
    d.quit()


if __name__ == '__main__':
    '''
    ele_dict = {'url':url, 'text_id':login_text, 'userid':'id_account_l',\
                'pwdid':'id_password_l', 'loginid':'login_btn','uname':account, 'pwd':pwd,\
                'errorid':'该账号格式不正确'}
    user_list = [{'uname':account, 'pwd':pwd}]
    '''
    ele_dict = get_webinfo(r'E:\Python汇总\自动化测试-selenium\source\webinfo.txt')
    # user_list = get_userinfo(r'C:\Users\hyg\Desktop\test\userinfo.txt')
    xinfo = XlUserinfo(r'E:\Python汇总\自动化测试-selenium\source\userinfo.xls')
    user_list = xinfo.get_sheetinfo_by_index(0)

    # file webinfo/usrinfo ele_dict= get_webinfo(path) user_list=get_userinfo(path)
    register_test(ele_dict, user_list)
