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