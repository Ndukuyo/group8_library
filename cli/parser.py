

import argparse

def create_parser():


    parser = argparse.ArgumentParser(
        description= "Hi, Welcome to group_8 library", 
        epilog= "Example, python3 -m cli.main add 'Atomic Habits' --author 'James Clear' --year 1997 --publisher 'Long Horn Publisher' " 
    )

    subparsers = parser.add_subparsers(
        dest= "command",        
        help= "Available commands",
        required= True
    )

   
    add_parser = subparsers.add_parser(
        "add",
        help= "Add a new book",
     
    )

    add_parser.add_argument(
        "title",                            
        help= "Please Enter Book Title"
    )

    add_parser.add_argument(
        "--author",
        required= True,
        help= "Plese Enter the Author's Name"
    )

    add_parser.add_argument(
        "--year",
        type= int,                     
        required=True,
        help= "Please Enter Year of Publication (e.g., 1997)"     
    )

    add_parser.add_argument(
        "--publisher",
        required= True,
        help= "Please Enter The Publisher's Name"
    )

    
    list_parser = subparsers.add_parser(
        "list",
        help= "View Our Catalogue"
    ) 

    
    search_parser = subparsers.add_parser(
        "search",
        help= "Search for books by title or author"
    )

    search_parser.add_argument(
        "keyword",
        help= "word to look for in title or author"
    )


    delete_parser = subparsers.add_parser(
        "delete",
        help= "Remove a book from Library by title"
    )

    delete_parser.add_argument(
        "book_title",
        help= "Title of the book to be deleted"
    )

    return parser  