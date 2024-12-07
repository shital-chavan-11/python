#swapping without using third variable
def swap(p,q):
    p=p+q
    q=p-q
    p=p-q
    print("p:",p)
    print("q",q)
a=int(input("enter the no:"))
b=int(input("enter the no:"))
swap(a,b)