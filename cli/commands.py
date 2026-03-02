
#the actual work each command does 

from storage import Library
from book_validation import check_title, check_author, check_year, check_publisher

#Initialize once

data = Library()

def cmd_add(args):
    # will handle the 'add' command
    print("\n ADDING BOOK ...")

    #validate title
    result = check_title(args.title)

    if result != "OK":
        print(result)
        return
    
    #validate author
    result = check_author(args.author)
 
    if result != "OK":
        print(result)
        return
    
    #validate year
    result = check_year( str(args.year) )
    
    if result != "OK":
        print(result)
        return
    
    #validate publisher
    result = check_publisher(args.publisher)

    if result != "OK":
        print(result)
        return
    
    data.add_book(args.title, args.author ,args.year, args.publisher)
    #print(f"Added: '{args.title}' by {args.author} \n {args.year} {args.publisher}")


def cmd_list(args):
    #will handle list command
    print("OUR BOOKS: ")

    books = data.books

    if not books:
        print("   No books yet. Add some with: python3 -m cli.main add ... ")
        return
    
    
    for book in books:
            print(f"   {book.title} by {book.author} {book.year} {book.publisher}")
            


def cmd_search(args):
    # will handle search command
    print(f"  SEARCHING FOR:  '{args.keyword}'")

    results = data.find_books(args.keyword)

    if not results:
        print("   No matching books found")
        return
    
    print(f"  Found {len(results)} books: ")
    for book in results:
        print(f"   {book.title} by {book.author} {book.year} {book.publisher}")


def cmd_delete(args):
    print(f"\n DELETING BOOK...")

    #find by title and delete 
    books = data.books

    i = 0
    for book in books:
        if book.title.lower() == args.book_title.lower():
            books.pop(i)
            data.save()               #save changes
            print(f"Deleted: '{args.book_title}'")
            return
        
        i = i + 1
        
    print(f"  No book with title '{args.book_title}' found")


