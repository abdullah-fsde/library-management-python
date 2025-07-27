class Library:
    def __init__(self,book):
        self.book = book
    def availableBooks(self):
        print("The books available at the library are :")
        for i,book in enumerate(self.book,start=1):
            print(f"{i}. {book}")
    def requestBook(self,name):
        self.name = name
        requestedbook=input("Enter the book you want to borrow: ")
        if requestedbook.islower():
            requestedbook = requestedbook.title()
        elif requestedbook.isupper():
            requestedbook = requestedbook.title()
        elif requestedbook.istitle():
            pass
        if requestedbook in self.book:
            print(f"The book {requestedbook} is issued to you ,Mr./Mrs. {name}")
            self.book.remove(requestedbook)
        elif requestedbook not in self.book:
            print(f"The book {requestedbook} is not in the library either because the book has been issued to somebody else or there maybe no books named {requestedbook}")
            take = input("Do you want to add this book to library? (Yes/No):")
            if take.islower():
                take = take.title()
            elif take.isupper():
                take = take.title()
            elif take.istitle():
                pass
            else:
                return False
            if take == "Yes":
                self.book.append(requestedbook)
                self.availableBooks()
            else:
                print("Thanks for your time")
    def returnorlendBook(self):
        addbook=input("Enter the Book you want to return or give it ot library :")
        addbook=addbook.title()
        self.book.append(addbook)
        print(f'"{addbook}" has been added to the library.')
class Student:
    def __init__(self,name):
        self.name = name
if __name__=="__main__":
    print("===== Welcome to DK's Library =====")
    studentname = input("Enter your name : ")
    if studentname.islower():
        studentname=studentname.title()
    name=Student(studentname)
    books= Library(["Python","PowerBI","Django","Social Studies","Science"])
    while(True):
        choice = int(input('''
    Choose an option:
    1. List books available
    2. Request a book to borrow
    3. Add/Return book to library
    4. Exit the library
                        
    Your choice: '''))
        print("\n")
        if choice == 1:
            books.availableBooks()
        elif choice == 2:
            books.availableBooks()
            books.requestBook(studentname)
        elif choice == 3:
            books.returnorlendBook()
            books.availableBooks()
        elif choice == 4:
            break
        else:
            print("Enter a valid choice please")
