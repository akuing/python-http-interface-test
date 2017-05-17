fo = open("statuscode.txt","r+",encoding="utf-8")
strLine= fo.readlines()
for str in strLine:
    print(str)
    list=str.split()
    print(list)

fo.close()