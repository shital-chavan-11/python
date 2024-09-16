#sum of first natural no by using recursion
def nat(num):
    if num==1 or num==0:
        return 1
    else:
        return num+nat(num-1)
p=int(input("enter the no"))
print(nat(p))