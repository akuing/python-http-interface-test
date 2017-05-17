import requests

strIP=input("请输入你要查询的IP地址：")

params={"ip":strIP}
result = requests.get("http://ip.taobao.com/service/getIpInfo.php",params=params)
# result = requests.post("http://ip.taobao.com/service/getIpInfo.php",data=params)
print("你输入的IP地址所在的国家："+result.json()["data"]["country"])
print("你输入的IP地址所在的地区："+result.json()["data"]["area"])
print("你输入的IP地址所在的省份："+result.json()["data"]["region"])
print("你输入的IP地址所在的城市："+result.json()["data"]["city"])
