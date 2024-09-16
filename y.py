#composite no
def compo(a):
    flag=0
    for i in range(1,a+1):
        if a%i==0:
            flag+=1
    if flag>2:
        print("this is composite no")
    else:
        print("this is not composite no")
s=int(input("enter the no"))
compo(s)