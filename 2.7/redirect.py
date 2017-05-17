import requests

jump=input("请输入重定向调转的次数（1-10之间的整数）：")
result = requests.get("http://httpbin.org/redirect/"+jump)

print(result.status_code)
count=1
for response in result.history:
    print("第{0}跳:Location={1}".format( count,response.headers["Location"]))
    count+=1
