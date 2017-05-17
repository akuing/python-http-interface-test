import requests


searchStr={"q":"python"}

result=requests.get("http://www.bing.com",params=searchStr)

print(result.url)
print(result.status_code)
# print(result.text)
