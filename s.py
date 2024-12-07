#sum of odd numbers in range of 1 to 100
def odd():
    sum=0
    for i in range(1,100):
        if(i%2!=0):
            sum+=i
    print(sum)
odd()