class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

books = [
    Book("a", "a", 2021),
    Book("b", "b", 2019),
    Book("c", "c", 2022)
]

for book in books:
    if book.year > 2020:
        print(f"{book.title} by {book.author}, {book.year}")
