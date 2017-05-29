#挑战问题
# 一个文件test1.txt，里面的数据如下：
# aaa
# bbb
# 希望在test12.txt里生成如下数据：
# https://baidu.com/web/list.jsp?keyword=aaa&cnt=10
# https://baidu.com/web/list.jsp?keyword=bbb&cnt=10

start='https://baidu.com/web/list.jsp?keyword='
end="&cnt=10"
fromFile = open('test1.txt','r')
toFile = open('test12.txt','w')
lines=fromFile.readlines()
for item in lines:
    resultStr=start+item.strip()+end+"\n"
    toFile.write(resultStr)
    print(resultStr)

fromFile.close()
toFile.close()
