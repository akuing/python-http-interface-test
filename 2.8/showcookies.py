import requests
import json

dictcookies={}
print("请输入一组cookie，格式为key=value，直接回车表示输入结束：")
strcookie=input()
while(len(strcookie.strip())>0) :
    listcookie=strcookie.split("=")
    if(len(listcookie)>1):
        dictcookies[listcookie[0]]=listcookie[1]
    else:
        print("请输入正确的cookie组，格式为key=value")


    strcookie=input()
result = requests.get("http://httpbin.org/cookies/delete?name",cookies=dictcookies)
#
print(json.dumps(result.json(),indent=4))
print(result.history[0].headers)
print(result.request.headers)