#string is anagram or not
def anagram(str,str1):
    flag=0
    for i in str:
        if i in str1:
            flag+=1
    if flag==len(str):
        print("this is anagram")
    else:
        print("this is not anagram")
p=input("enter the first string:")
q=input("enter the second string:")
anagram(p,q)


    