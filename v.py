#prime number using recursion

def prime(n):
  flag=0
  
  if n==0 or n==1:
          return 1
  else:
          if n%n==0 :
               flag+=1
               prime(n-1)
          if(flag==2):
          
               print("this is prime no") 
          else:
               print("this is not prime no")              
          

prime(5)          

    