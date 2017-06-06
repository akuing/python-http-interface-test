#挑战问题
# 从一个list数据结构中查找指定的对象，返回对象的序号和对象本身，找不到的情况下返回False
# list=[1,3,'444',55,88,'99','aa']
def SearchList(inputStr,list):
    for item in range(len(list)):
        if (list[item] == inputStr):
            return (item, inputStr)

        try:
            if(list[item] == int(inputStr)):
                return (item, inputStr)
            else:
                continue
        except:
            continue

    return False
inputStr = input("请输入你要查找的内容：")
list=[1,3,'444',55,88,'99','aa']
result = SearchList(inputStr,list)
print(result)