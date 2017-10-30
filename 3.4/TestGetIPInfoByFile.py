import unittest
import requests
import time
import re

class TestGetIPInfoByFile(unittest.TestCase):
    testcaseList=[]
    def getCityFromIP(self,ipStr):
        params = {"ip": ipStr}
        result = requests.get("http://ip.taobao.com/service/getIpInfo.php", params=params)
        return result.json()["data"]
    def testRunTheCase(self):
        self.loadTestCaseFromFile("测试案例1.txt")
        self.loadTestCaseFromFile("测试案例2.txt")
        self.loadTestCaseFromFile("测试案例3.txt")
        for caseDict in self.testcaseList:
            time.sleep(3)
            with self.subTest(msg=caseDict["案例意图"]):
                result=self.getCityFromIP(caseDict["ip"])
                if(isinstance(result,str)):
                    self.assertEqual(caseDict["expect"],result,caseDict["案例意图"])
                else:
                    self.assertEqual(caseDict["expect"],result["city"],caseDict["案例意图"])
    def loadTestCaseFromFile(self,fileName):
        with open(fileName,"r") as file:
            testItem = {}
            for line in file:
                if(re.match("\s*#",line)):
                    continue
                result = re.match(r'\s*\"([^\"]+)\"\s*:\s*\"([^\"]+)\"', line)
                if(result != None):
                    testItem[result.group(1)]=result.group(2)
                if(re.match(r"\s*-{3,}",line)):
                    self.testcaseList.append(testItem.copy())
                    testItem={}
                    continue



