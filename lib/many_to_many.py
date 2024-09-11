class Author:
       def __init__(self,name):
        self.name = name

        
       def books(self):
            return [contract.book for contract in Contract.all if contract.author == self]
       def sign_contract(self,book,date,royalties):
           return Contract(self,book,date,royalties)
       def total_royalties(self):
            royalties = [contract.royalties for contract in Contract.all if contract.author == self]
            
            return sum(royalties)

           
           
       def contracts(self):
            return [contract for contract in Contract.all if contract.author == self]



class Book:
    def __init__(self,title):
        self.title = title

    def contracts(self):
        return [ contract for contract in Contract.all  if contract.book == self]
    
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]



class Contract:
       all = []
       def __init__(self,author,book,date, royalties):
        if isinstance(author, Author):
            self.author = author
        else :
            raise TypeError("course must be an instance of Author") 
        if isinstance(book, Book):
            self.author = author
        else :
            raise TypeError("course must be an instance of Book") 
        if not isinstance(date,str):
            raise TypeError("course must be an instance of String") 
        if not isinstance(royalties,int):
            raise TypeError("course must be an instance of Int") 
            
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

       @classmethod
       def contracts_by_date(cls,date):
           return [contract for contract in cls.all if contract.date == date]
              

author1 = Author("Name 1")
book1 = Book("Title 1")
book2 = Book("Title 2")
book3 = Book("Title 3")
author2 = Author("Name 2")


book4 = Book("Title 4")
contract1 = Contract(author1, book1, "02/01/2001", 10)
contract2 = Contract(author1, book2, "01/01/2001", 20)
contract3 = Contract(author1, book3, "03/01/2001", 30)
contract4 = Contract(author2, book4, "01/01/2001", 40)

# print(contract1.contracts_by_date("01/01/2001"))
print(author1.total_royalties())
