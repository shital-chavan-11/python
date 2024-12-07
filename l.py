#prime no in given range
def prime(a,b):
    flag=0
    for i in range(a,b+1):
        for j in range(1,i+1):
            if(i%j==0):
                flag+=1
        if flag==2:
            print(i)
        else:
            print("there is a no prime number in this range")    
p=int(input("enter the starting range:"))
q=int(input("enter the ending range:"))
prime(p,q)