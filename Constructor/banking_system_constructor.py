class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = False

    def display_info(self):
        status = "Borrowed" if self.is_available else "Available"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")

    def mark_borrow(self):
        if not self.is_available:
            self.is_available = True
            print(f"{self.is_available} has been marked as borrowed.")  # Fixed wording
        else:
            print(f"{self.is_available} is already borrowed.")

book1 = Book("1984", "Georj Orwell")
book1.display_info()
book1.mark_borrow()
book1.display_info()