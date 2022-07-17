from .. import db

class User:
    def __init__(self):
        pass

    def __init__(self, id, username, phone):
        self.id = id
        self.username = username
        self.phone = phone

def get_users_list():
    result = db.execute('SELECT * FROM user;')

    users = []
    for row in result:
        users.append(User(row['id'], row['username'], row['phone']))

    return users

def insert_user(user_info):
    db.execute(f'INSERT INTO user (username, phone) VALUES ("{user_info.username}", "{user_info.phone}");')
    return

def search_user(username):
    result = db.execute(f'SELECT * FROM user WHERE username LIKE "%{username}%";')

    users = []
    for row in result:
        users.append(User(row['id'], row['username'], row['phone']))

    return users

def delete_user(ids):
    for id in ids:
        db.execute(f'DELETE FROM user WHERE id="{id}";')

    return