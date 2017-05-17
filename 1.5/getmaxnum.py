strInput= input("请输入三个数字，用空格分开：")
num1,num2,num3=[int(n) for n in strInput.split()]

if(num1 >= num2 and num1 >= num3):
    print("您输入的最大的是数字为："+str(num1))
elif(num2>=num1 and num2>=num3):
    print("您输入的最大的是数字为：" + str(num2))
else:
    print("您输入的最大的是数字为：" + str(num3))