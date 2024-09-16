#composite no in given range
def compo(a,b):
    flag=0
    for i in range(a,b+1):
        for j in range(1,b+1):
            if(i%j==0):
              flag+=1
    if flag>2:
        print(i)
p=int(input("enter the starting no"))
q=int(input("enter the ending no"))
compo(p,q)