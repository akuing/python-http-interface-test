import unittest
import requests
import time

class TestGetIPInfo(unittest.TestCase):
    testcaseList=[{"msg":"ReturnGoodWhenGetIpInfoGivenNormalIPInBeijing","ip":"124.126.228.193","expect":"北京市"},
                  {"msg": "ReturnErrorMsgWhenGetIpInfoGivenInvalidIP", "ip": "124.126.228.", "expect": "invaild ip."}]
    def getCityFromIP(self,ipStr):
        params = {"ip": ipStr}
        result = requests.get("http://ip.taobao.com/service/getIpInfo.php", params=params)
        return result.json()["data"]
    def testRunTheCase(self):
        for caseDict in self.testcaseList:
            time.sleep(3)
            with self.subTest(msg=caseDict["msg"]):
                result=self.getCityFromIP(caseDict["ip"])
                if(isinstance(result,str)):
                    self.assertEqual(caseDict["expect"],result,caseDict["msg"])
                else:
                    self.assertEqual(caseDict["expect"],result["city"],caseDict["msg"])

    # def testShouldReturnGoodWhenGetIpInfoGivenNormalIPInJinan(self):
    #     params={"ip":"124.128.111.111"}
    #     result = requests.get("http://ip.taobao.com/service/getIpInfo.php",params=params)
    #     self.assertEqual("济南市",result.json()["data"]["city"])
    # def testShouldReturnErrorMsgWhenGetIpInfoGivenInvalidIP(self):
    #     params={"ip":"124.126.228."}
    #     result = requests.get("http://ip.taobao.com/service/getIpInfo.php",params=params)
    #     self.assertEqual("invaild ip.",result.json()["data"])