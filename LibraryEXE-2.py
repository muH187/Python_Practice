class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBooks(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The library has {self.noBooks} Books right now:")
        for book in self.books:
            print(book)

l = Library()
l.addBooks("Harry Potter1")
l.addBooks("Harry Potter2")
l.addBooks("Harry Potter3")
l.addBooks("Harry Potter4")
l.addBooks("Harry Potter5")
l.addBooks("Harry Potter6")
l.showInfo()