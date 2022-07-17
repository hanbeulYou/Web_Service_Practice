from .. import db

class Book:
    def __init__(self):
        pass

    def __init__(self, id, title, author, publisher, isbn):
        self.id = id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.isbn = isbn

def get_book_list():
    result = db.execute('SELECT * FROM book;')

    books = []
    for row in result:
        books.append(Book(row['id'], row['title'], row['author'], row['publisher'], row['isbn']))

    return books

def insert_book(book_info):
    db.execute(f'INSERT INTO book (title, author, publisher, isbn) VALUES ("{book_info.title}", "{book_info.author}", "{book_info.publisher}", "{book_info.isbn}");')

    return

def search_book(title):
    result = db.execute(f'SELECT * FROM book WHERE title LIKE "%{title}%";')

    books = []
    for row in result:
        books.append(Book(row['id'], row['title'], row['author'], row['publisher'], row['isbn']))

    return books

def delete_book(ids):
    for id in ids:
        db.execute(f'DELETE FROM book WHERE id="{id}";')

    return