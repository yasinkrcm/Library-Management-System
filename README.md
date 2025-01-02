<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Library Management System</title>
</head>
<body>
    <h1>Library Management System</h1>
    <p><strong>Welcome to the Library Management System project!</strong> This Python-based application allows you to manage books in a library. You can add new books, view the list of available books, and remove books using a simple menu interface. This system is designed to be intuitive and easy to use, making it perfect for library management tasks.</p>
    <h2>Table of Contents</h2>
    <ol>
        <li><a href="#description">Description</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#file-structure">File Structure</a></li>
        <li><a href="#contributing">Contributing</a></li>
    </ol>
    <h2 id="description">Description</h2>
    <p>The Library Management System is a simple console application written in Python. It allows users to:</p>
    <ul>
        <li>Add books to a library.</li>
        <li>List all the books in the library.</li>
        <li>Remove books from the library by their unique ID.</li>
    </ul>
    <p>The application stores book data in a text file named <code>books.txt</>, which contains information about each book, such as its title, author, release year, and the number of pages.</p>

    <h2 id="features">Features</h2>
    <p>This system provides the following features:</p>
    <ul>
        <li><strong>Add Book</strong>: Allows you to add a new book with details like title, author, release year, and pages.</li>
        <li><strong>List Books</strong>: Displays all books currently stored in the library with their ID, title, author, and number of pages.</li>
        <li><strong>Remove Book</strong>: Allows you to remove a book by providing its unique ID.</li>
    </ul>

    <h2 id="installation">Installation</h2>
    <h3>Prerequisites</h3>
    <p>To run this project, you need to have Python 3.x installed on your computer. You can download and install Python from <a href="https://www.python.org/downloads/" target="_blank">here</a>.</p>

    <h3>Steps to Install</h3>
    <ol>
        <li>Clone the repository from GitHub to your local machine:</li>
        <pre><code>git clone https://github.com/yasinkrcm/Library-Management-System.git</code></pre>
        
        <li>Navigate to the project directory:</li>
        <pre><code>cd Library-Management-System</code></pre>
        
        <li>The only requirement is Python 3.x, so ensure that Python is installed and available in your system's PATH.</li>
        
        <li>Run the program with the following command:</li>
        <pre><code>python library_management_system.py</code></pre>
    </ol>

    <h2 id="usage">Usage</h2>
    <p>Once the program is running, you will see a menu with the following options:</p>
    <ul>
        <li><strong>List Books</strong> - View a list of all the books in the library.</li>
        <li><strong>Add Book</strong> - Add a new book to the library with its details.</li>
        <li><strong>Remove Book</strong> - Remove a book from the library using its ID.</li>
        <li><strong>Quit</strong> - Exit the program.</li>
    </ul>

    <h3>Example Interaction</h3>
    <h4>Adding a Book:</h4>
    <pre><code>
    Book title: The Great Gatsby
    Book author: F. Scott Fitzgerald
    First release year: 1925
    How many pages: 218
    Book added successfully!
    </code></pre>

    <h4>Removing a Book:</h4>
    <pre><code>
    Enter the ID of the book you want to remove: 1
    Book with ID '1' removed successfully!
    </code></pre>

    <h2 id="file-structure">File Structure</h2>
    <p>The project has the following file structure:</p>
    <pre><code>
    Library-Management-System/
    ├── library_management_system.py  # Main Python program
    ├── books.txt                    # Data file containing books information
    └── README.md                    # Documentation file (this file)
    </code></pre>
    <p>All book data is stored in the <code>books.txt</code> file. Each book's details are separated by commas in the following order: ID, title, author, release year, and number of pages.</p>

    <h2 id="contributing">Contributing</h2>
    <p>If you want to contribute to this project, feel free to fork the repository and submit pull requests. If you find any issues or have suggestions for new features, please open an issue in the GitHub repository. Contributions are always welcome!</p>

    <p><strong>Note:</strong> Ensure that you test your changes thoroughly before submitting a pull request.</p>

    <footer>
        <p>Thank you for using the Library Management System!</p>
    </footer>

</body>
</html>
