# coding=utf-8
#######################################################
#请回答为什么这个程序不能达到playcookies.py同样的效果？
#请修改这个程序，达到书中2.9小节的挑战问题的要求
#来自学习者 @李嘉睿
#######################################################

import requests
import json

print("add key=value ，用于增加cookies")
print("del key，用于删除cookies")
print("show，用于显示当前的cookies")
print("quit, 退出")

operate = input("请输入cookies指令：\n")
global r
s= requests.Session()
dict = {}

while True:
    if operate.split(" ")[0] == "add":
        content = operate.split(" ")[1].split("=")
        dict[content[0]] = content[1]
        r = s.get("http://httpbin.org/cookies/set?", cookies=dict)
        #print(print(json.dumps(r.json(), indent=4, ensure_ascii=False)))

    elif operate.split(" ")[0] == "del":
        content = operate.split(" ")[1].split("=")
        dict[content[0]] = None
        r = s.get("http://httpbin.org/cookies/delete?", cookies=dict)
        #print(print(json.dumps(r.json(), indent=4, ensure_ascii=False)))

    elif operate.split(" ")[0] == "show":
        r = s.get("http://httpbin.org/cookies")
        print(json.dumps(r.json(), indent=4))

    elif operate.split(" ")[0] == "quit":
        break
    else:
        print("你输入的命令"+operate+"不合法")
    operate=input("")
