import json

name = input("请输入你的姓名：")
phone = input("请输入你的电话：")
dict = {"name" : name,"phone":phone}

print(json.dumps(dict, indent=4,ensure_ascii=False))
