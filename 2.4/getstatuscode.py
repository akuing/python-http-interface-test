import requests

urlpath=input("请输入你要发送HTTP请求的URL链接：")
try:
    result=requests.get(urlpath)
    print("你得到的返回码是："+str(result.status_code))
except (requests.ConnectionError):
    print("你输入的HTTP请求地址："+urlpath+" 出现链接异常，请确认地址是否正确！")