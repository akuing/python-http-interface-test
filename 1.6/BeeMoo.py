

def getBeeMooResult(num):
    if(num % 2 ==0 and num %3 == 0):
        return "BeebeebeeMoomoomoo"
    if(num % 2 ==0):
        return "Beebeebee"
    if(num % 3 ==0):
        return "Moomoomoo"
    return num

if(__name__ == '__main__'):
    minNum = input("请输入区间最小值：")
    maxNum = input("请输入区间最大值：")
    for num in range(int(minNum),int(maxNum)):
        print(getBeeMooResult(num))