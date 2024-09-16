#greater number among the the numbers
def great(a,b,c):
    if a>b and a>c:
        print(a,"is greater")
    if b>a and b>c:
        print(b,"is greater")
    if c>a and c>b:
        print(c,"is greater")
p=int(input("enter the no:"))
q=int(input("enter the no:"))
r=int(input("enter the no:"))
great(p,q,r)