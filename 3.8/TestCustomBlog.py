import unittest
import requests
from bs4 import BeautifulSoup

class TestCustomBlog(unittest.TestCase):
    def getCsrf_token(self,session):
        result = session.get("http://localhost:5000/login")
        soup = BeautifulSoup(result.text, "html.parser")
        inputs = soup.find_all("input", id="csrf_token")
        for input in inputs:
           return input.attrs['value']
    def testLoginShouldReturnLoggedInSuccessfullyGivenNormalGoodUserInfo(self):
        session = requests.session()
        params={'email':'a_kui@163.com','password':'111111','csrf_token':self.getCsrf_token(session)}
        result = session.post("http://localhost:5000/login",data=params)
        soup=BeautifulSoup(result.text,"html.parser")
        self.assertRegex(soup.prettify(),'Logged in successfully',msg="登录成功验证")
