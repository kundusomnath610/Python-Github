def add_book(title, available_books):
    if title not in available_books:
        available_books.append(title)

def search_book(title, available_books):
    if title in available_books:
        print(f"'{title}' is available in the library.")  
    else:
        print(f"Sorry, '{title}' is not available in the library.")

def view_books(available_books):
    print(f"Available books: {available_books}")

# Sample usage
available_books = ['Harry Potter', '1984', 'Pride and Prejudice']

# View current books (before adding)
view_books(available_books)

# Add a new book
add_book('The Grate Gatsby', available_books)

# View books again to confirm the new addition
view_books(available_books)

# Search for a book that exists
search_book('1984', available_books)

# Search for a book that doesn't exist
search_book('The Catcher in the Rye', available_books)
