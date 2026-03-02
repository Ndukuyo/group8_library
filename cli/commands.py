
#the actual work each command does 

from pheobes_file import Library_data
from filsans_file import validations

#Initialize once

data = Library_data()
validator = validations()

def cmd_add(args):
    # will handle the 'add' command
    print("\n ADDING BOOK ...")

    #validate title
    ok, msg = validator.check_title(args.title)
    if not ok:
        print(msg)
        return
    
    #validate author
    ok, msg = validator.check_author(args.author)
    if not ok:
        print(msg)
        return
    
    #validate year
    ok, msg = validator.check_year( str(args.year) )
    if not ok:
        print(msg)
        return
    
    #validate publisher
    ok, msg = validator.check_publisher(args.publisher)
    if not ok:
        print(msg)
        return
    
    data.add_book(args.title, args.author ,args.year, args.publisher)
    print(f"Added: '{args.title}' by {args.author} '\n' {args.year} {args.publisher}")


def cmd_list(args):
    #will handle list command
    print("OUR BOOKS: ")

    books = data.get_all_books()

    if not books:
        print("   No books yet. Add some with: python3 -m cli.main add ... ")
        return
    
    for book in books:
        if args.details:
            #Detailed view 
            print(f" \n ID: {book[ 'id']}")
            print(f"   Title: {book[ 'title']}")
            print(f"   Author: {book[ 'author']}")
            print(f"   Year: {book[ 'year']}")
            print(f"   Publisher: {book[ 'publisher']}")
        else:
            #Simple view
            print(f"   {book['id']}. {book['title']} by {book['author']} {book['year']} {book['publisher']}")


def cmd_search(args):
    # will handle search command
    print("  SEARCHING FOR:  '{args.keyword}'")

    results = data.search_books(args.keyword)

    if not results:
        print("   No matching books found")
        return
    
    print(f"  Found {len(results)} books: ")
    for book in results:
        print(f"   {book['title']} by {book['author']} {book['year']} {book['publisher']}")


def cmd_delete(args):
    print(f"\n DELETING BOOK...")

    #find by id and delete 
    books = data.get_all_books()
    for i, book in enumerate(books):
        if book['id'] == args.book_id:
            title = book['title']
            books.pop(i)
            data.save_books()               #save changes
            print(f"Deleted: '{title}'")
            return
        
    print(f"  No book with title {args.book_title} found")


#commands to functions

COMMAND_FUNCTIONS = {
    "add": cmd_add,
    "list": cmd_list,
    "search": cmd_search,
    "delete": cmd_delete
}
