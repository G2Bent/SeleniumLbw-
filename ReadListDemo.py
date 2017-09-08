#conding:utf-8
import codecs
def get_webinfo(path):
    web_info = { }
    #这种方法解析文档会出现乱码问题
    # config = open(path)
    #Python给我们解决了解析文档问题的方法
    config = codecs.open(path,'r','utf-8')
    for line in config:
        result = [ele.strip() for ele in line.split("=")]
        # result = line.split("=")
        # web_info.update(dict([result]))
        # print(result)
    return web_info

def get_userinfo(path):
    #定义一个元组，用于存放后面的字典
    user_info = []
    #打开一个路径的文件，以可读形式，编码格式为utf-8
    config = codecs.open(path,'r','utf-8')
    #每一行读出来的数据都存放在一个字典里面
    for line in config:
        #这里我们就定义一个字典
        user_dict = { }
        #通过";"将"uname和pwd"数据分开（;号是文档里面的）
        result = [ele.strip() for ele in line.split(';')]
        #对元素进行循环
        for r in result:
            # 循环=号，将uname和对应里面的数据分开，另外pwd和pwd的数据分开
            account = [ele.strip() for ele in r.split("=")]
            #每循环一次都更新一次
            user_dict.update(dict([account]))
            #将user_dict的结果保存到user_info里面
        user_info.append(user_dict)
            # print(account)
    return user_info

if __name__ =='__main__':

    webinfo = get_webinfo(r"webinfo.txt")
    for key in webinfo:
        print(key,webinfo[key])

    userinfo = get_userinfo(r"E:\Python汇总\自动化测试-selenium\source\userinfo.txt")
    for l in userinfo:
        print(l)
    # print(userinfo)