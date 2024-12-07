import random
list=[]
class books():
    def __init__ (self,info):
        self.book_name=info[0]
        self.book_writer=info[1]
        self.publish_year=info[2]
        self.coppies=info[3]
        self.generate_ISBN()
    def generate_ISBN(self):
        select=input("select your books:1)newer2)older:")
        if select=="1":
            print("your book is newer so you get the 13 digit ISBN no")
            ISBN=random.randint(1000000000000,9999999999999)
            print(ISBN)
        else:
            print("your book is older so you get the 10 digit ISBN no")
            ISBN=random.randint(1000000000,9999999999)
            print(ISBN)
        self.category()
    def category(self):
        print("There are serveral types of the books. they are depend on the writer to writer")        
print("enter your books details: ")
book_name=input("enter your book name:")
book_writer=input("enter book writer name:")
publish_year=input("enter the book publish year:")
coppies=int(input("enter the how many coppies are sold:"))
info=[book_name,book_writer,publish_year,coppies]
obj=books(info)

