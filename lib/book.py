class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.current_page = 0

    def turn_page(self, page):
        self.current_page = page

