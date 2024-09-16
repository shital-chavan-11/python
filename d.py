#prime number
def prime(a):
    flag=0
    if a==1:
        print()
    for i in range(1,a+1):
        if a%i==0:
            flag+=1
    if flag==2:
        print("this is prime no")
    else:
        print("this is not prime no")
c=int(input("enter the no:"))
prime(c)