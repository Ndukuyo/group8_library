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
            'publisher' : self.publisher
        }
    
class Library:
    def __init__(self):
        self.books = []
        self.load_books()