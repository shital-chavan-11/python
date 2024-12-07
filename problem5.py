import random
class Car():
    def __init__ (self,info):
        self.name=name
        self.color=color
        self.founder=founder
        self.buy_date=buy_date
        self.gen_no(name)
    def gen_no(self,name):
        no=random.randint(1000,9999)
        unique=str(no)
        st="MH"
        car_no=st+unique
        print("your car no is ",car_no)       
print("enter your car details here :")
name=input("enter the car name")
color=input("enter the color of car")
founder=input("enter the founder name")
buy_date=input("enter the buy date")
info=[name,color,founder,buy_date]
obj=Car(info)