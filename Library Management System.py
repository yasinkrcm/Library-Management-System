class Library:
    def getBooks(self):
        try:
            books = []
            file = open("books.txt","r+",encoding="utf-8")
            for book in file:
                book = book.splitlines()[0].split(",")
                books.append(book)
            file.close()
            return books
        except:
            print("books.txt not exist")
    
    
    def listBooks(self):
        books = self.getBooks()
        if books:
            for book in books:
                if len(book) >= 5:  
                    print(f"{book[0]} - Book Title: {book[1]}, Book Author: {book[2]}, Pages: {book[4]}")
                else:
                    print("Incomplete book data.")
        else:
            print("No books in library.Please add book into books")
            return 1

    def addBook(self):
            title = input("Book title : ")
            author = input("Book author : ")
            releaseyear = input("First release year : ")
            pages = input("How many pages : ")
            id = 1
            with open("books.txt","a+",encoding="utf-8") as file :
                for book in file:
                    id +=1 
                    books = []
                    book = book.splitlines()[0].split(",")
                    books.append(book)
                file.write(f"{int(id)},{title},{author},{releaseyear},{pages}\n")
            print("\nBook added successfully!")

    def removeBook(self):
        if self.listBooks():
            return 1
        else:
            id = input("Enter the iD of the book you want to remove: ")
            books = []
            with open("books.txt", "r", encoding="utf-8") as file:
                for book in file:
                    book = book.strip().splitlines()[0].split(",")
                    books.append(book)
            with open("books.txt", "w", encoding="utf-8") as file:
                for book in books:
                    if book[0] != id:
                        file.write(f"{','.join(book)}\n")
                    else:
                        print(f"\nBook '{book[1]}' removed successfully!")
        

lib = Library()

while True:
    choice = input(
"""\n*** MENU***
1) List Books
2) Add Book
3) Remove Book 
4) Quit
Enter your choice (1-4): """)
    
    if choice == "1" :
        lib.listBooks()
    elif choice == "2":
        lib.addBook()
    elif choice == "3":
        lib.removeBook()
    elif choice == "4" :
        break    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")