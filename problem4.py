#students details
import random
class Student():
    def __init__ (self,info,name,aadhar_no):
        self.name=name
        self.aadhar_no=aadhar_no
        self.physics=info[0]
        self.chemistry=info[1]
        self.biology=info[2]
        self.math=info[3]
        self.geography=info[4]
        self.avg() 
        self.exam_no(self.name,self.aadhar_no)
    def avg(self):
        average=((self.physics+self.chemistry+self.biology+self.math+self.geography)/5)
        print(average)
        self.place(average)
    def place(self,average):
        if average>=60:
            print("you get the first class")
        elif average>=50:
            print("you get the second class")
        elif average>=40:
            print("you get the third class")
        else:
            print("you fail in the exam")
       
    def exam_no(self,name,aadhar_no):
        s=random.randint(100000,999999)
        no=str(s)
        unique=aadhar_no[6:12]+no
        print(name,"your exam no is",unique)       
print("enter your matks here:")
name=input("enter your name :")
aadhar_no=(input("enter your aadhar no:"))
physics=int(input("enter the marks"))
chemistry=int(input("enter the marks:"))
biology=int(input("enter the marks"))
math=int(input("enter the marks"))
geography=int(input("enter the marks"))
info=[physics,chemistry,biology,math,geography]
obj=Student(info,name,aadhar_no)

