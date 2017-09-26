from public.Hg_Exception import *
import json,urllib.request
def verify_code(code):
    code_dict = None
    if "@" in str(code):
        url = 'http://112.74.29.84:23301/api/User/getemailverifycode?email='+str(code)+'&type=1'
    else:
        url = 'http://112.74.29.84:23301/api/User/getphoneverifycode?phone='+str(code)+'&type=1'
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
def email_code(code):
    code_dict = None
    if '@' in str(code):
        url = 'http://112.74.29.84:23301/api/User/getemailverifycode?email='+str(code)+'&type=3'
    else:
        url = 'http://112.74.29.84:23301/api/User/getphoneverifycode?phone='+str(code)+'&type=3'
    try:
        code_dict=json.loads(urllib.request.urlopen(url).read())
    except Exception as e:
        print(e)
    # print(code_dict)
    if code_dict != None:
        if code_dict['success'] == True:
            # print(code_dict['data']['verifycode'])
            return code_dict['data']['verifycode']
        else:
            raise ApiStateException
    else:
        raise ApiOpenException
