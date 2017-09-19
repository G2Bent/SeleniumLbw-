from public.Hg_Exception import *
import json,urllib.request
def verify_code(phone):
    code_dict = None
    url = 'http://120.25.81.114:23301/api/User/getphoneverifycode?phone='+str(phone)+'&type=1'
    try:
        code_dict = json.loads(urllib.request.urlopen(url).read())
    except Exception as e :
        print (e)
    if code_dict != None:
        if code_dict['success'] == True:
            return code_dict['data']['verifycode']
        else:
            raise ApiStateException
    else:
        raise ApiOpenException

#获取德雅个人信息邮箱绑定验证码
def email_code(email):
    code_dict = None
    url = 'http://192.168.2.72:5001/api/User/getemailverifycode?email='+str(email)+'&type=3'
    try:
        code_dict=json.loads(urllib.request.urlopen(url).read())
    except Exception as e:
        print(e)
    print(code_dict)
    if code_dict != None:
        if code_dict['success'] == True:
            print(code_dict['data']['verifycode'])
            return code_dict['data']['verifycode']
        else:
            return ('接口异常')
    else:
        return ('code_dict值为None')