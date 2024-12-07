#given no is binary or not
def bina(str):
    flag=0
    p=len(str)
    
    for i in str:
        if i=="0" or i=="1":
            flag=flag+1
    if flag==p:
        print("this is binary no")
    else:
        print("this is not binary no")
str2=input("enter the string")
bina(str2)
            