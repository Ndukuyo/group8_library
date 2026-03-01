def check_title(title):
    title = title.strip()
    if title == "":
        return "ERROR: Please enter a title"
    if len(title) < 2:
        return "ERROR: Title must be at least 2 characters"
    return "OK"

def check_author(author):
    author = author.strip()
    if author == "":
        return "ERROR: Please enter an author"
    if len(author) < 2:
        return "ERROR: Author name must be at least 2 characters"
    return "OK"

def check_year(year):
    year = year.strip()
    if year == "":
        return "ERROR: Please enter a year"
    if not year.isdigit():
        return "ERROR: Year should be numbers only"
    
    year_num = int(year)
    if year_num < 1800:
        return "ERROR: Year must be 1800 or later"
    if year_num > 2026:   # 
        return "ERROR: Year cannot be in the future"
    
    return "OK"

def check_publisher(publisher):
    publisher = publisher.strip()
    if publisher == "":
        return "ERROR: Please enter a publisher"
    if len(publisher) < 2:
        return "ERROR: Publisher must be at least 2 characters"
    return "OK"

def check_all_book_info(title, author, year, publisher):
    result = check_title(title)
    if result != "OK":
        return result

    result = check_author(author)
    if result != "OK":
        return result

    result = check_year(year)
    if result != "OK":
        return result

    result = check_publisher(publisher)
    if result != "OK":
        return result

    return "OK"

# --- TEST BLOCK ---
if __name__ == "__main__":
    print(check_title("Hobbit"))
    print(check_author("Tolkien"))
    print(check_year("1937"))
    print(check_publisher("Allen & Unwin"))

    print(check_all_book_info("Hobbit", "Tolkien", "1937", "Allen & Unwin"))