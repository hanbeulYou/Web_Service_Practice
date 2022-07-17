from flask import render_template
from .models import book

def list_book():
    books = book.get_book_list()

    return render_template('list_book.html', books=books)

def add_book(info):
    book.insert_book(book.Book(0, info['title'], info['author'], info['publisher'], info['isbn']))
    

def search_book(info):
    books = book.search_book(info['title'])

    return render_template('list_book.html', books=books)

def delete_book(info):
    book.delete_book(info)