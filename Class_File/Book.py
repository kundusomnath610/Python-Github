class Book:
    def __init__(self, title, author):  # Fixed: __init__ instead of __int__
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display_info(self):
        status = "Not Available" if self.is_borrowed else "Available"  # Fixed logic
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")

    def mark_borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"{self.title} has been marked as borrowed.")  # Fixed wording
        else:
            print(f"{self.title} is already borrowed.")

# Creating a book instance with title and author
book1 = Book("1984", "George Orwell")
book1.display_info()

book1.mark_borrow()
book1.display_info()
