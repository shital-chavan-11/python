#factorial
def fcat(n):
    k=1
    for i in range(1,n+1):
        k=k*i
    print(k)
c=int(input("enter the no:"))
fcat(c)
    