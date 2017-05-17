def printMsg(statuscode,strStatusType):
    dictStatusDesp={"1XX": "信息，服务器收到请求，需要请求者继续执行操作",
                    "2XX": "成功，操作被成功接收并处理",
                    "3XX": "重定向，需要进一步的操作以完成请求",
                    "4XX": "客户端错误，请求包含语法错误或无法完成请求",
                    "5XX": "服务器错误，服务器在处理请求的过程中发生了错误"
                    }
    print("你输入的状态码" + str(statuscode) + "属于"+strStatusType+"类")
    print("分类描述："+dictStatusDesp[strStatusType])

def getInput():
    statuscode=input("请输入你要查询的状态码：")
    while not statuscode.isdigit() or int(statuscode)<100 or int(statuscode)>=600:
        print("输入的状态码不合法，合法的状态码为100 - 599之间的数字。")
        statuscode = input("请输入你要查询的状态码：")
    else:
        return statuscode

statuscode= int(getInput())
if statuscode>=100 and statuscode <199 :
    printMsg(statuscode,"1XX")
elif statuscode>=200 and statuscode <299 :
    printMsg(statuscode, "2XX")
elif statuscode>=300 and statuscode <399 :
    printMsg(statuscode, "2XX")
elif statuscode>=400 and statuscode <499 :
    printMsg(statuscode, "2XX")
elif statuscode>=500 and statuscode <599 :
    printMsg(statuscode, "2XX")


