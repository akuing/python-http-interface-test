import unittest
import os
import shutil
import re
import HTMLTestRunner
import requests

from bs4 import BeautifulSoup


class TestCustomBlog(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("C:\\MyWork\\myGitHub\\custom-blog\\app.db.bk")
        except (FileNotFoundError):
            pass;
        shutil.copy("C:\\MyWork\\myGitHub\\custom-blog\\app.db", "C:\\MyWork\\myGitHub\\custom-blog\\app.db.bk")

    def tearDown(self):
        shutil.copy("C:\\MyWork\\myGitHub\\custom-blog\\app.db.bk", "C:\\MyWork\\myGitHub\\custom-blog\\app.db")

    def testRegistShouldSuccessGivenNormalInput(self):
        result = self.getResultByUserPasswd("test2@163.com", "111111")
        self.assertEqual(200, result.status_code, "status_code should be 200")
        soup = BeautifulSoup(result.text, "html.parser")
        returnStr = soup.find_all("li")[0].get_text()
        self.assertRegex(returnStr, "Registered successfully")

    def testRegistShouldFailGivenDuplicateUserAgain(self):
        result = self.getResultByUserPasswd("test@163.com", "111111")
        self.assertEqual(200, result.status_code, "status_code should be 200")
        soup = BeautifulSoup(result.text, "html.parser")
        returnStr = soup.find_all("li")[0].get_text()
        self.assertRegex(returnStr, "Such user already is avalable")

    def testRegistShouldFailGivenDifferentPassword(self):
        result = self.getResultByUserPasswd("test@163.com", "111111", "222222")
        self.assertEqual(200, result.status_code, "status_code should be 200")
        soup = BeautifulSoup(result.text, "html.parser")
        returnStr = soup.find_all("span", attrs={"class": "error"})[0].get_text()
        self.assertRegex(returnStr, "Passwords must match")

    def testLoginShouldSuccessGivenNormalUserAndPassword(self):
        result = self.getLoginResultByUserPasswd("a_kui@163.com", "111111")
        self.assertEqual(200, result.status_code)
        soup = BeautifulSoup(result.text, "html.parser")
        resultStr = soup.find("li").get_text()
        self.assertRegex(resultStr, "Logged in successfully")

    def testLoginShouldFailedGivenBadPassword(self):
        result = self.getLoginResultByUserPasswd("a_kui@163.com", "222222")
        self.assertEqual(200, result.status_code)
        soup = BeautifulSoup(result.text, "html.parser")
        resultStr = soup.find("li").get_text()
        self.assertRegex(resultStr, "Wrong credentials")

    def testLoginShouldFailedGivenBadUserEmail(self):
        result = self.getLoginResultByUserPasswd("abcd", "111111")
        self.assertEqual(200, result.status_code)
        soup = BeautifulSoup(result.text, "html.parser")
        resultStr = soup.find("span", attrs={"class": "error"}).get_text()
        self.assertRegex(resultStr, "Invalid email address.")

    def getResultByUserPasswd(self, username, password, cpassword=""):
        if (len(cpassword) == 0):
            cpassword = password
        session = requests.session()
        result = session.get("http://127.0.0.1:5000/register")
        soup = BeautifulSoup(result.text, "html.parser")
        csrf_token = soup.find_all("input", id="csrf_token")[0].attrs["value"]
        data = {"csrf_token": csrf_token, "email": username, "password": password, "cpassword": cpassword}
        result = session.post("http://127.0.0.1:5000/register", data=data)
        return result

    def getLoginResultByUserPasswd(self, username, password):
        session = requests.session()
        result = session.get("http://127.0.0.1:5000/login")
        soup = BeautifulSoup(result.text, "html.parser")
        csrf_token = soup.find_all("input", id="csrf_token")[0].attrs["value"]
        data = {"csrf_token": csrf_token, "email": username, "password": password}
        result = session.post("http://127.0.0.1:5000/login", data=data)
        return result


if (__name__ == "__main__"):
    # methodList  = unittest.TestLoader().getTestCaseNames(TestCustomBlog())
    # suite = unittest.TestSuite();
    # for methodname in methodList:
    #     if(re.match("testRegist",methodname)):
    #         suite.addTest(TestCustomBlog(methodName=methodname))
    #         print(methodname)
    # print(suite)
    # result = unittest.TestResult()
    # suite.run(result=result)
    # print(result)

    # 定义一个测试容器
    test = unittest.TestSuite()

    # 将测试用例，加入到测试容器中
    methodList = unittest.TestLoader().getTestCaseNames(TestCustomBlog())
    for methodname in methodList:
        if (re.match("test", methodname)):
            test.addTest(TestCustomBlog(methodName=methodname))

    # 定义个报告存放的路径，支持相对路径
    file_path = "result.html"
    file_result = open(file_path, 'w', encoding="utf-8")

    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=file_result, title="测试", description="用例执行情况")
    # runner = unittest.TextTestRunner(stream=file_result,verbosity=4)

    unittest.main(testRunner=runner)
    # 运行测试用例
    # runner.run(test)
    file_result.close()
