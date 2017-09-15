class ApiOpenException(Exception):
    def __init__(self,err='验证码返回值为空，接口异常！'):
        Exception.__init__(self,err)

class ApiStateException(Exception):
    def __init__(self,err='接口返回的状态不为True！'):
        Exception.__init__(self,err)