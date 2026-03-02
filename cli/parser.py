# where all my argeparse commands will go

import argparse

# the main parser with all subcommands
def create_parser():

    #main parser
    parser = argparse.ArgumentParser(description= "Hi, Welcome to group_8 library", epilog= "Example, python -m cli.main add 'Atomic Habits' --author 'James Clear' --year 1997 --publisher 'Long Horn Publisher' " )

    # (subcommands) menu options
    subparsers = parser.add_subparsers(
        dest= "command",        
        help= "Available commands",
        required= True
    )

    # 1st command: ADD BOOK ==
    add_parser = subparsers.add_parser(
        "add",
        help= "Add a new book",
        aliases= ["new", "create"] 
    )

    add_parser.add_argument(
        "title",                            #positional arg (required)
        help= "Please Enter Book Title"
    )

    add_parser.add_argument(
        "--author",
        required= True,
        help= "Plese Enter the Author's Name"
    )

    add_parser.add_argument(
        "--year",
        type= int,                      #converts input to int
        required=True,
        help= "Please Enter Year of Publication (e.g., 1997)"     
    )

    add_parser.add_argument(
        "--publisher",
        required= True,
        help= "Please Enter The Publisher's Name"
    )

    #2nd command: LIST BOOKS ==
    list_parser = subparsers.add_parser(
        "list",
        aliases = ['show', 'all'],
        help= "View Our Catalogue"
    ) 

    #3rd command: SEARCH BOOKS 
    search_parser = subparsers.add_parser(
        "search",
        help= "Search for books by title or author"
    )

    #4th command: DELETE BOOKS
    delete_parser = subparsers.add_parser(
        "delete",
        help= "Remove a book from Library by id"
    )

    delete_parser.add_argument(
        "book_id",
        type= int,
        help= "ID number of the book to be deleted"
    )

    return parser  