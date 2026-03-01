import json
import os

DATA_FILE = 'library.json'

class Book:
    def __init__(self, title, author, year, publisher):
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        
    def to_dict(self):
        return {
            'title' : self.title,
            'author' : self.author,
            'year' : self.year,
            'publisher' : self.publisher,
        }
    
class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def add_book(self, title, author, year, publisher):
        book = Book(title, author, year, publisher) 
        self.books.append(book)
        self.save()
        print(f'Book "{title}" added to the library.')

    def save(self):
        data = [book.to_dict() for book in self.books]
        with open(DATA_FILE, 'w') as file:
            json.dump(data, file, indent=4)

    def load_books(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                data = json.load(file)
                for item in data:
                    book = Book(
                        title=item['title'],
                        author=item['author'],
                        year=item['year'],
                        publisher=item['publisher']
                    )
                    self.books.append(book)

    def find_book(self, search):
        results = []
        search = search.lower()

        for book in self.books:
            if (search in book.title.lower() or 
                search in book.author.lower() or 
                search in book.publisher.lower()):
                results.append(book)

        return results
    
    def view_books(self):
        for book in self.books:
            print(f'Title: {book.title}, Author: {book.author}, Year: {book.year}, Publisher: {book.publisher}')

    def main():
        library = Library()
        while True:
            print("\nLibrary Management System")
            print("1. Add Book")
            print("2. View Books")
            print("3. Search Books")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                year = input("Enter publication year: ")
                publisher = input("Enter publisher: ")
                library.add_book(title, author, year, publisher)
            elif choice == '2':
                library.view_books()
            elif choice == '3':
                search = input("Enter search term (title, author, or publisher): ")
                results = library.find_book(search)
                if results:
                    for book in results:
                        print(f'Title: {book.title}, Author: {book.author}, Year: {book.year}, Publisher: {book.publisher}')
                else:
                    print("No books found.")
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    Library.main()

    