class Book:
    def __init__(self, title):
        self.title = title

book1 = Book('Bible')
book2 = Book('Aku Ankka')

class Libarary:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, Book):
        self.books.append(Book)

libarary1 = Libarary('Helsinki')
libarary2 = Libarary('Vantaa')

libarary1.add_book(book1)
libarary1.add_book(book2)
libarary2.add_book(book1)

for book in libarary1.books:
    print(book.title)


