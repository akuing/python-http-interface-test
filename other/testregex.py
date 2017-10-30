import re
string = "今天的天气真好明天是2017年9月6日吃什么呢？"
result = re.search(r"\d+年\d+月\d+日",string)
print(result.group(0))