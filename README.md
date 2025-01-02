# Library Management System

**Welcome to the Library Management System project!** This Python-based application allows you to manage books in a library. You can add new books, view the list of available books, and remove books using a simple menu interface. This system is designed to be intuitive and easy to use, making it perfect for library management tasks.

## Table of Contents
1. [Description](#description)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [File Structure](#file-structure)
6. [Contributing](#contributing)

## Description
The Library Management System is a simple console application written in Python. It allows users to:
- Add books to a library.
- List all the books in the library.
- Remove books from the library by their unique ID.

The application stores book data in a text file named `books.txt`, which contains information about each book, such as its title, author, release year, and the number of pages.

## Features
This system provides the following features:
- **Add Book**: Allows you to add a new book with details like title, author, release year, and pages.
- **List Books**: Displays all books currently stored in the library with their ID, title, author, and number of pages.
- **Remove Book**: Allows you to remove a book by providing its unique ID.

## Installation

### Prerequisites
To run this project, you need to have Python 3.x installed on your computer. You can download and install Python from [here](https://www.python.org/downloads/).

### Steps to Install
1. Clone the repository from GitHub to your local machine:
    ```bash
    git clone https://github.com/yasinkrcm/Library-Management-System.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Library-Management-System
    ```
3. The only requirement is Python 3.x, so ensure that Python is installed and available in your system's PATH.
4. Run the program with the following command:
    ```bash
    python "Library Management System.py"

    ```

## Usage
Once the program is running, you will see a menu with the following options:
- **List Books**: View a list of all the books in the library.
- **Add Book**: Add a new book to the library with its details.
- **Remove Book**: Remove a book from the library using its ID.
- **Quit**: Exit the program.

### Example Interaction

#### Adding a Book:

Book title: The Great Gatsby
Book author: F. Scott Fitzgerald
First release year: 1925
How many pages: 218<br>
Book added successfully!


#### Removing a Book:


Enter the ID of the book you want to remove: 1<br>
Book with ID '1' removed successfully!


## File Structure

The project has the following file structure:

<p>

Library-Management-System/<br><br>
├── library_management_system.py  # Main Python program<br>
├── books.txt                    # Data file containing books information<br>
└── README.md                    # Documentation file (this file)<br>
</p>

All book data is stored in the `books.txt` file. Each book's details are separated by commas in the following order: ID, title, author, release year, and number of pages.

## Contributing

If you want to contribute to this project, feel free to fork the repository and submit pull requests. If you find any issues or have suggestions for new features, please open an issue in the GitHub repository. Contributions are always welcome!

**Note:** Ensure that you test your changes thoroughly before submitting a pull request.



Thank you for using the Library Management System!
