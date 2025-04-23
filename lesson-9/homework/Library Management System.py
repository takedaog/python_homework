class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_name, book_title):
        member = None
        for m in self.members:
            if m.name == member_name:
                member = m
        if member == None:
            print("Member not found")
            return
        
        if len(member.borrowed_books) >= 3:
            raise MemberLimitExceededException("Can't borrow more than 3 books")
        
        book = None
        for b in self.books:
            if b.title == book_title:
                book = b

        if book == None:
            raise BookNotFoundException("Book not found in library")
        
        if book.is_borrowed:
            raise BookAlreadyBorrowedException("Book is already borrowed")
        
        book.is_borrowed = True
        member.borrowed_books.append(book)

    def return_book(self, member_name, book_title):
        for m in self.members:
            if m.name == member_name:
                for b in m.borrowed_books:
                    if b.title == book_title:
                        b.is_borrowed = False
                        m.borrowed_books.remove(b)
                        return
        print("Book or member not found")

# --- TESTING ---
lib = Library()

book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("1984", "George Orwell")
lib.add_book(book1)
lib.add_book(book2)

member1 = Member("Tom")
lib.add_member(member1)

try:
    lib.borrow_book("Tom", "Harry Potter")
    lib.borrow_book("Tom", "1984")
    lib.borrow_book("Tom", "Nonexistent Book")  # should raise exception
except Exception as e:
    print("Error:", e)
