from .. import db

class Borrow:
    def __init__(self):
        pass

    def __init__(self, id, userid, bookid, check_out):
        self.id = id
        self.userid = userid
        self.bookid = bookid
        self.check_out = check_out

def get_borrow_list():
    result = db.execute('SELECT * FROM borrow;')

    list = []
    for row in list:
        list.append(Borrow(row['id'], row['userid'], row['bookid'], row['check_out']))

    return list

def insert_borrow(borrow_info):
    db.execute(f'INSERT INTO borrow (userid, bookid) VALUES ("{borrow_info.userid}", "{borrow_info.bookid}");')

    return

# def search_borrow_bytitle(title):
#     result = db.execute(f'SELECT * FROM borrow WHERE bookid LIKE "%{title}%";')

#     books = []
#     for row in result:
#         books.append(Book(row['id'], row['title'], row['author'], row['publisher'], row['isbn']))

#     return books

# def delete_book(ids):
#     for id in ids:
#         db.execute(f'DELETE FROM book WHERE id="{id}";')

#     return