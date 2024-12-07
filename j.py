#palindrome
def pal(str):
    str1=""
    for i in str:
        str1=i+str1
    if(str1==str):
        print("this is palindrome")
    else:
        print("this is not palindrome")
str2=input("enter the string:")
pal(str2)