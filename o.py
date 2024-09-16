#perfect number or not
def perfect(a):
    sum=0
    for i in range(1,a):
        if(a%i==0):
            sum=sum+i
    if sum==a:
        print("this is perfect no")
    else:
        print("thids is not perfect no")
c=int(input("enter the no"))
perfect(c)