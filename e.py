#armstrong number
def arm(a):
    temp=a
    order=len(str(a))
    sum=0
    while a>0:
        digit=temp%10
        sum=sum+digit**order
        temp//=10
    if sum==a:
        print("this is armstrong no")
    else:
        print("this is not armstrong")  
b=int(input("enter the no:"))
arm(b)    