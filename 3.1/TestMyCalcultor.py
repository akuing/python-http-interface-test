import unittest

from MyCalcultor import MyCalculator


class TestMyCalculator(unittest.TestCase):
    def testShouldReturnGoodWhenDivideGivenTwoPositiveNumber(self):
        myCalculator = MyCalculator()
        self.assertEqual(4,myCalculator.divide(8,2))
    def testShouldReturnGoodWhenDivideGivenTwoPositiveNumberCannotBeDivideToEnd(self):
        myCalculator = MyCalculator()
        self.assertEqual(4,myCalculator.divide(9,2))
    def testShouldReturnGoodWhenDivideGivenTwoPositiveNumberInString(self):
        myCalculator = MyCalculator()
        self.assertEqual(4,myCalculator.divide("9","2"))
    def testShouldReturnStringPleaseInputRightParamWhenDivideGivenTwoPositiveFloatNumberInString(self):
        myCalculator = MyCalculator()
        self.assertEqual("请输入正确的参数，参数必须是整数型或者可以转换为整数型的字符串",
                         myCalculator.divide("9.8","2.1"))
    def testShouldReturnStringPleaseInputRightParamWhenDivideGivenTwoPositiveFloatNumber(self):
        myCalculator = MyCalculator()
        self.assertEqual("请输入正确的参数，参数必须是整数型或者可以转换为整数型的字符串",
                         myCalculator.divide(9.8,2.1))
    def testShouldReturnStringDivisorCannotBeZeroWhenDivideGivenZeroToParam2(self):
        myCalculator = MyCalculator()
        self.assertEqual("除数不能为零",myCalculator.divide(9,0))

    def testShouldReturnStringPleaseInputRightParamWhenDivideGivenNonNumberString(self):
        myCalculator = MyCalculator()
        self.assertEqual("请输入正确的参数，参数必须是整数型或者可以转换为整数型的字符串",
                         myCalculator.divide("ssd","dd"))
    def testShouldReturnStringPleaseInputRightParamWhenDivideGivenNonNumberString(self):
        myCalculator = MyCalculator()
        self.assertEqual("请输入正确的参数，参数必须是整数型或者可以转换为整数型的字符串",
                         myCalculator.divide("ssd","11"))
    def testShouldReturnStringPleaseInputRightParamWhenDivideGivenDictAndList(self):
        myCalculator = MyCalculator()
        self.assertEqual("请输入正确的参数，参数必须是整数型或者可以转换为整数型的字符串",
                         myCalculator.divide({"as":"value"},[11,2,2]))