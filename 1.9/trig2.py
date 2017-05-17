
high = int(input("请输入塔高"))

for line in range(1,high):
    print(" "*(high-line)+"*"*(line*2-1))