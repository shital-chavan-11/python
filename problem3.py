# monthly Expensive 
class Man():
    def __init__ (self,info):
        self.first_week=info[0]
        self.second_week=info[1]
        self.third_week=info[2]
        self.forth_week=info[3]
        self.weak1=info[4]
        self.weak2=info[5]
        self.weak3=info[6]
        self.weak4=info[7]
        self.man()
      
    def man(self):
        totalm=self.first_week+self.second_week+self.third_week+self.forth_week
        print("The total expensive in the case of man:",totalm)
        totalw=self.weak1+self.weak2+self.weak3+self.weak4
        print("The total expensive in the case of women:",totalw)
        self.guess(totalm,totalw)
       

    def guess(self,totalm,totalw):
        if totalm>totalw:
            self.last1()
        else:
            self.last2()
    def last1(self):
        print("The expensive of the man is greater than women")
        self.first()
    def last2(self):
        print("The expensive  of the women is greater than man")
        self.last()
    def first(self):
        print("women is win")
    def last(self):
        print("man is win")
print("enter below Details:")
first_week=int(input("enter your expense in the first weak:"))
second_week=int(input("enter your expense in the second weak:"))
third_week=int(input("enter your expense in the third weak:"))
forth_week=int(input("enter your expense in the forth weak:"))
weak1=int(input("enter your expense in the first weak:"))
weak2=int(input("enter your expense in the second weak:"))
weak3=int(input("enter your expense in the third weak:"))
weak4=int(input("enter your expense in the forth weak:"))
info=[first_week,second_week,third_week,forth_week,weak1,weak2,weak3,weak4]
obj=Man(info)

