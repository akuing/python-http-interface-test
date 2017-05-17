import unittest
from StatusCodeType import StatusCodeType
# import StatusCodeType
class TestStatusCodeType(unittest.TestCase):
    errorStr="输入错误，请输入100-599之间的数字"
    statustype=StatusCodeType()
    def testShouldReturnErrorWhenGetStatusTypeGivenNonNumber(self):
        self.assertEqual(self.errorStr,self.statustype.getStatusType("abc"))
    def testShouldReturnErrorWhenGetStatusTypeGivenNumberNotBetween100To599(self):
        self.assertEqual(self.errorStr,self.statustype.getStatusType("1111"))
    def testShouldReturn1XXWhenGetStatusTypeGivenNumberBetween100To199(self):
        strReturn='''你输入的状态码{0}属于1XX类\n分类描述：信息，服务器收到请求，需要请求者继续执行操作'''
        self.assertEqual(strReturn.format("111"),self.statustype.getStatusType("111"))
    def testShouldReturn2XXWhenGetStatusTypeGivenNumberBetween200To299(self):
        strReturn='''你输入的状态码{0}属于2XX类\n分类描述：成功，操作被成功接收并处理'''
        self.assertEqual(strReturn.format("211"),self.statustype.getStatusType("211"))
    def testShouldReturn3XXWhenGetStatusTypeGivenNumberBetween300To399(self):
        strReturn='''你输入的状态码{0}属于3XX类\n分类描述：重定向，需要进一步的操作以完成请求'''
        self.assertEqual(strReturn.format("333"),self.statustype.getStatusType("333"))
    def testShouldReturn4XXWhenGetStatusTypeGivenNumberBetween400To499(self):
        strReturn='''你输入的状态码{0}属于4XX类\n分类描述：客户端错误，请求包含语法错误或无法完成请求'''
        self.assertEqual(strReturn.format("400"),self.statustype.getStatusType("400"))
    def testShouldReturn5XXWhenGetStatusTypeGivenNumberBetween500To599(self):
        strReturn='''你输入的状态码{0}属于5XX类\n分类描述：服务器错误，服务器在处理请求的过程中发生了错误'''
        self.assertEqual(strReturn.format("535"),self.statustype.getStatusType("535"))