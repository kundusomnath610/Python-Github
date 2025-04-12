def checkout_book(title, available_books):
    if title in available_books:
        available_books.remove(title)

def return_book(title, available_books):
    if title not in available_books:
        available_books.append(title)

def view_books(available_books):
    print(f"Available books: {available_books}")

# Example usage:
available_books = ['Harry Potter', '1984', 'Pride and Prejudice']

view_books(available_books)
checkout_book('Harry Potter', available_books)
view_books(available_books)
return_book('Harry Potter', available_books)
view_books(available_books)
