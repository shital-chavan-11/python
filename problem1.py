#ecommerce website rendering connections 
list=[]
import random
class User():
    def __init__ (self,info):
        self.name=info[0]
        self.username=info[1]
        self.email=info[2]
        self.date_of_birth=info[3]
        self.address=info[4]
        self.password=info[5]
        self.confirm_password=info[6]
        self.secretKey()
    def secretKey(self):
        s=random.randint(10000,99999)
        string=str(s)
        unique=self.password+string
        print(unique)
        if unique not in list:
            list.append(unique)
        print(list)
        self.login()
    def login(self):
        print("select the identity:normal_user and super_user")
        user=input("enter the identity of the User:")
        if user=="normal_user":
            print("you are the normal user you rendering to the user dashbooard!!")
        if user=="super_user":
            print("you are the superuser you rendering to the superuser dashbooard!!")
        self.work()
    def work(self):
        print("if the user is superuser then they are the superadmin of teh web page they are create the product for the normal user also the update and delete the produect")
        self.logout()
    def logout(self):
        print("superuer and the normaluser is also logout by the button of logout")
    
print("Enter the details of the user-"),
name=input("Enter the name of the User:"),
username=input("Enter the username:"),
email=input("Enter the User EMail:"),
date_of_birth=input("Enter the BOD of User:"),
address=input("Enter the Address of User:"),
password=input("Enter the Password of User:")
confirm_password=input("Enter the confirm Password of User:")
info=[name,username,email,date_of_birth,address,password,confirm_password]
obj=User(info)

