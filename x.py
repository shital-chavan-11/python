#classes & objects
class student:
    print("these are marks of students")
    def __init__ (self,roll_no,name,marks):
        self.roll_no=roll_no
        self.name=name
        self.marks=marks
        
    def show(self):
        print(self.roll_no)
        print(self.name) 
        print(self.marks)       
stud=student(1,"shital",99)
stud1=student(2,"ram",98)
stud.show() 
stud1.show() 
           
        