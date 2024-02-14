class Library:
    def listbooks(self):
        try:
            with open("books.txt","r",encoding="utf-8") as file:
                for book in file:
                    book = book.splitlines()[0].split(",")
                    books = []
                    books.append(book)
                    print(f"Book Title : {books[0][0]} , Book Author : {books[0][1]} ")
        except FileNotFoundError:
                    print("\nPlease add a book to the file")
                
    def addbook(self):
            title = input("Book title : ")
            author = input("Book author : ")
            releaseyear = input("First release year : ")
            pages = input("How many pages : ")
            with open("books.txt","+a",encoding="utf-8") as file :
                file.write(f"{title},{author},{releaseyear},{pages}\n")
            print("\nBook added successfully!")

    def removebook(self,):
        title = input("Enter the title of the book you want to remove: ")
        books = []
        try :
            with open("books.txt", "r", encoding="utf-8") as file:
                for book in file:
                    book = book.strip().splitlines()[0].split(",")
                    books.append(book)
            with open("books.txt", "w", encoding="utf-8") as file:
                for book in books:
                    if book[0] != title:
                        file.write(f"{','.join(book)}\n")
                        print(f"\nBook '{title}' removed successfully!")
        except FileNotFoundError:
             print("\nPlease add a book to the file")
        

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
        lib.listbooks()
    elif choice == "2":
        lib.addbook()
    elif choice == "3":
        lib.removebook()
    elif choice == "4" :
        break    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")