#character is vowel or consonant
def string(s):
    if s =="a" or s=="e" or s=="i" or s=="o" or s=="u" or s=="A" or s=="E"  or s=="O" or s=="I" or s=="U":
        print("this character is vowel")
    else:
        print("this character is consonant")
p=input("enter the character:")
string(p)