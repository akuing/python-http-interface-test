import unittest
import requests
import time
import re
import pyexcel

class TestGetIPInfoWithExcel(unittest.TestCase):
    testcaseList=[]
    def getCityFromIP(self,ipStr):
        params = {"ip": ipStr}
        result = requests.get("http://ip.taobao.com/service/getIpInfo.php", params=params)
        return result.json()["data"]
    def testRunTheCase(self):
        self.testcaseList = pyexcel.iget_records(file_name="测试案例集1-获取IP地址的地理信息.xlsx")
        print(self.testcaseList)
        for caseDict in self.testcaseList:
            time.sleep(3)
            with self.subTest(msg=caseDict["案例意图"]):
                result=self.getCityFromIP(caseDict["ip"])
                if(isinstance(result,str)):
                    self.assertEqual(caseDict["expect"],result,caseDict["案例意图"])
                else:
                    self.assertEqual(caseDict["expect"],result["city"],caseDict["案例意图"])

