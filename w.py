#classes & objects
class books:
    print("these are some books which are i liked")
  
    def __init__(self,book_name,writer,star):
        self.book_name=book_name
        self.writer=writer
        self.star=star
    def show(self):
        print(self.book_name)
        print(self.writer)
        print(self.star)
book1=books("three mistakes of my life","brown",5)
book2=books("three mistakes of my life","brown",7)
book1.show()
book2.show()