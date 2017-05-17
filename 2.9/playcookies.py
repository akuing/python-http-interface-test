import requests
import json
url="http://httpbin.org/cookies"

commanddesp='''请输入cookies指令：
add key=value ，用于增加cookies
del key       ，用于删除cookies
show          ，用于显示当前的cookies
quit          , 退出
'''
def printresult(result):
    print(json.dumps(result.json(),indent=4))

def addcookie(strcookie,session):
    printresult(session.get(url+"/set?"+strcookie))

def deletecookie(strcookie,session):
    printresult(session.get(url+"/delete?"+strcookie))

def showcookies(session):
    printresult(session.get(url))

session=requests.session()
command=input(commanddesp)
while(command):
    if(command.split()[0]=='add'):
        addcookie(command.split()[1],session)
    elif (command.split()[0]=='del'):
        deletecookie(command.split()[1],session)
    elif(command=="show"):
        showcookies(session)
    elif(command=="quit"):
        break
    else:
        print(commanddesp)
    command=input()






#
# result = session.get(url+"/set?name=dsfdsf&name1=111")
# print("statuscode:"+str(result.status_code))
# print("result:",result.json())
# print("request.cookies",json.loads(str(result.request.headers).replace('\'','\"'))["Cookie"])
# dictcookies = requests.utils.dict_from_cookiejar(result.cookies)
# print("result.cookies",json.dumps(dictcookies))
# print("result.history:".join(str(x.status_code) for x in result.history))
# print("-"*10)
# result = session.get(url)
#
# print("result:",result.json())
# print("request.cookies",json.loads(str(result.request.headers).replace('\'','\"'))["Cookie"])
# dictcookies = requests.utils.dict_from_cookiejar(result.cookies)
# print("result.cookies",json.dumps(dictcookies))
# print("-"*10)
#
# result = session.get(url+"/delete?name")
# print("result:",result.json())
# print("request.cookies",json.loads(str(result.request.headers).replace('\'','\"'))["Cookie"])
# print("result.header",result.headers)
# dictcookies = requests.utils.dict_from_cookiejar(result.cookies)
# print("result.cookies",json.dumps(dictcookies))
# print("-"*10)