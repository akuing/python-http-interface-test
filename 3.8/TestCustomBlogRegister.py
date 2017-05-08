import unittest
import requests
from bs4 import BeautifulSoup

class TestCustomBlogRegister(unittest.TestCase):
    def testRegistShouldSuccessGivenNormalInput(self):
        result = self.getResultByUserPasswd("test@163.com", "111111")
        self.assertEqual(200,result.status_code,"status_code should be 200")
        soup = BeautifulSoup(result.text,"html.parser")
        returnStr =  soup.find_all("li")[0].get_text()
        self.assertRegex(returnStr,"Registered successfully")

    def testRegistShouldFailGivenDuplicateUserAgain(self):
        result = self.getResultByUserPasswd("test@163.com","111111")
        self.assertEqual(200,result.status_code,"status_code should be 200")
        soup = BeautifulSoup(result.text,"html.parser")
        returnStr =  soup.find_all("li")[0].get_text()
        self.assertRegex(returnStr,"Such user already is avalable")

    def testRegistShouldFailGivenDifferentPassword(self):
        result = self.getResultByUserPasswd("test@163.com","111111","222222")
        self.assertEqual(200,result.status_code,"status_code should be 200")
        soup = BeautifulSoup(result.text,"html.parser")
        returnStr =  soup.find_all("span",attrs={"class":"error"})[0].get_text()
        self.assertRegex(returnStr,"Passwords must match")

    def getResultByUserPasswd(self,username,password,cpassword=""):
        if(len(cpassword)==0):
            cpassword=password
        session = requests.session()
        result = session.get("http://127.0.0.1:5000/register")
        soup = BeautifulSoup(result.text, "html.parser")
        csrf_token = soup.find_all("input", id="csrf_token")[0].attrs["value"]
        data = {"csrf_token": csrf_token, "email":username, "password": password, "cpassword": cpassword}
        result = session.post("http://127.0.0.1:5000/register", data=data)
        return result