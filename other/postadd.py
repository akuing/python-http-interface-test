import requests
import json

numbers={"num1":"11111a1","num2":-23}

result= requests.post("http://mock-api.com/WmnEBEKJ.mock/postadd",data=json.dumps(numbers))
# result= requests.post("http://mock-api.com/WmnEBEKJ.mock/postadd",data="ssd")


print(result.status_code)
print(result.text)
