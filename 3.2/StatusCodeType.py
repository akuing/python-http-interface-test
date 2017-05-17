class StatusCodeType:
    errorStr ="输入错误，请输入100-599之间的数字"
    normalStr = "你输入的状态码{0}属于{1}类\n分类描述：{2}"
    msgDict = {"1XX": "信息，服务器收到请求，需要请求者继续执行操作",
               "2XX": "成功，操作被成功接收并处理",
               "3XX": "重定向，需要进一步的操作以完成请求",
               "4XX": "客户端错误，请求包含语法错误或无法完成请求",
               "5XX": "服务器错误，服务器在处理请求的过程中发生了错误"
               }
    def getStatusType(self, param):
        if(param.isdigit()==False):
            return self.errorStr
        elif( int(param) <100 or int(param) >599):
            return self.errorStr
        return self.normalStr.format(param,param[0]+"XX",self.msgDict[param[0]+"XX"])
