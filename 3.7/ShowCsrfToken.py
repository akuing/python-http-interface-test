import requests
from bs4 import BeautifulSoup

class ShowCsrfToken:
    def showtoken(self):
        result= requests.session().get("http://127.0.0.1:5000/register")
        soup=BeautifulSoup(result.text,"html.parser")
        inputs= soup.find_all("input",id="csrf_token")
        # inputs= htmlParser.find_all("input",attrs={"name": "csrf_token"})
        for input in inputs:
            print("csrf_token属性的值（value）："+input.attrs["value"])
        # input = htmlParser.find("input",attrs={"name": "csrf_token"})
        # # print(input.attrs["value"])
        # print(input)

if __name__ == '__main__':
    showcsrftoken= ShowCsrfToken()
    showcsrftoken.showtoken()
