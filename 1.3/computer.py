def addnum(num1,num2):
    return num1+num2

if __name__ == '__main__':
    num1=input("请输入第一个数字：")
    num2=input("请输入第二个数字：")
    # num2=int(num2)
    print("两个数之和为：%s"  % addnum(int(num1),int(num2)))
