import requests
import json

numbers={"num1":"11","num2":-23}

# result= requests.post("http://mock-api.com/WmnEBEKJ.mock/postcondition",data=json.dumps(numbers))
result= requests.post("http://mock-api.com/WmnEBEKJ.mock/postcondition",data="ssd")

print(result.status_code)
print(result.text)
