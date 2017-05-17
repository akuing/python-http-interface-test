import math
class MyCalculator(object):
    def divide(self, param, param1):
        if(isinstance(param,int) or isinstance(param,str)) \
                and (isinstance(param1,int) or isinstance(param1,str)):
            try:
                if(isinstance(param,str)):
                    param=int(param)
                if(isinstance(param1,str)):
                    param1=int(param1)
            except(ValueError):
                return "请输入正确的参数，参数必须是整数型或者可以转换为整数型的字符串"
            try:
                return math.trunc(param/param1)
            except(ZeroDivisionError):
                return "除数不能为零"
        else:
            return "请输入正确的参数，参数必须是整数型或者可以转换为整数型的字符串"

