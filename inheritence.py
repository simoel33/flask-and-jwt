
class Bookshelf:
    def __init__(self,name,*books):
        self.name = name
        self.books = books

    def __str__(self):
        return f"BookShelf Name: {self.name} N° of books {len(self.books)}"

    def showBooks(self):
        for book in self.books:
            bk = Book(book)
            print(f"{bk.name}  this is Book")

class Book:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


book = Book("Harry Pooter")
book2 = Book("Intersteller")
list = [book,book2]

bookshelf = Bookshelf("Ibn Al Khatib",*list)
print(bookshelf)
bookshelf.showBooks()        
        