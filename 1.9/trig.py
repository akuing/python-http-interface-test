
high = int(input("请输入塔高"))

for line in range(1,high):
    for col in range(1,high-line+1):
        print(" ",end="")
    for star in range(1,line*2):
        print("*",end="")
    print("")