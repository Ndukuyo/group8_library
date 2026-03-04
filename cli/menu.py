import sys
from cli.commands import cmd_add, cmd_list, cmd_search, cmd_delete

def display_menu():

    print("          WELCOME TO GROUP 8 LIBRARY ")

    print("1,  Add a new book")
    print("2,  List all books ")
    print("3, Searrch for a book")
    print("4,  Delete a book ")
    print("5,  Quit")

def get_user_choice():

    while True:
        try:
            choise = input(" \n Enter your choise (1 - 5) ").strip()
            if choise in ['1', '2', '3', '4', '5']:
                return choise
            else:
                print("Invalid choice, please enter a number between 1-5 ")

        except KeyboardInterrupt:
            print(" \n\nGoodbye ")
            sys.exit(0)

def get_book_details():

    print("\n   Enter Book Details  ")
    title = input("Title: ").strip()
    author = input("Author: ").strip()

    while True:
        try:
            year = int(input("year: ").strip() )
            break
        except ValueError:
            print("Please enter a valid year (e.g., 2022)")

    publisher = input("Publisher: ").strip()

    return title, author, year, publisher


def run_menu():
    """Main menu loop"""
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == '1': 
            title, author, year, publisher = get_book_details()
            
           
            class Args:
                pass
            args = Args()
            args.title = title
            args.author = author
            args.year = year
            args.publisher = publisher
            
            cmd_add(args)
            
        elif choice == '2': 
            class Args:
                pass
            args = Args()
            cmd_list(args)
            
        elif choice == '3': 
            keyword = input("Enter search keyword: ").strip()
            if keyword:
                class Args:
                    pass
                args = Args()
                args.keyword = keyword
                cmd_search(args)
            else:
                print("Search keyword cannot be empty!")
                
       
                
        elif choice == '4':  
           
            class ListArgs:
                pass
            list_args = ListArgs()
            cmd_list(list_args)
            
           
            title = input("\nEnter the title of the book to delete: ").strip()
            if title:
                class Args:
                    pass
                args = Args()
                args.book_title = title
                cmd_delete(args)
            else:
                print("Book title cannot be empty!")
                
        elif choice == '5':  
            print("\nThank you for using Group 8 Library. Goodbye!")
            break
        
        input("\nPress Enter to continue...") 



