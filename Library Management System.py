class Library:
    def getBooks(self):
        try:
            books = []
            with open("books.txt", "r+", encoding="utf-8") as file:
                for book in file:
                    book = book.strip().split(",")
                    books.append(book)
            return books
        except FileNotFoundError:
            print("books.txt does not exist.")
            return []

    def listBooks(self):
        books = self.getBooks()
        if books:
            for book in books:
                if len(book) >= 5:  
                    print(f"{book[0]} - Book Title: {book[1]}, Book Author: {book[2]}, Pages: {book[4]}")
                else:
                    print("Incomplete book data.")
        else:
            print("No books in library. Please add a book.")

    def addBook(self):
        title = input("Book title: ")
        author = input("Book author: ")
        releaseyear = input("First release year: ")
        pages = input("How many pages: ")

        books = self.getBooks()
        if books:
            last_id = max(int(book[0]) for book in books)
        else:
            last_id = 0

        new_id = last_id + 1

        with open("books.txt", "a+", encoding="utf-8") as file:
            file.write(f"{new_id},{title},{author},{releaseyear},{pages}\n")
        
        print("\nBook added successfully!")

    def removeBook(self):
        books = self.getBooks()
        if not books:
            print("\nNo books in library to remove.")
            return

        book_id = input("Enter the ID of the book you want to remove: ")
        book_found = False

        updated_books = []
        with open("books.txt", "r", encoding="utf-8") as file:
            for book in file:
                book = book.strip().split(",")
                if book[0] != book_id:
                    updated_books.append(book)
                else:
                    book_found = True
        
        if book_found:
            with open("books.txt", "w", encoding="utf-8") as file:
                for book in updated_books:
                    file.write(f"{','.join(book)}\n")
            print(f"\nBook with ID '{book_id}' removed successfully!")
        else:
            print(f"\nBook with ID '{book_id}' not found.")

lib = Library()

while True:
    choice = input(
        """\n*** MENU ***
1) List Books
2) Add Book
3) Remove Book 
4) Quit
Enter your choice (1-4): """
    )
    
    if choice == "1":
        lib.listBooks()
    elif choice == "2":
        lib.addBook()
    elif choice == "3":
        lib.removeBook()
    elif choice == "4":
        break    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
