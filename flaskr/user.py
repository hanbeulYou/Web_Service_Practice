from flask import render_template
from .models import user

def list_user():
    users = user.get_users_list()

    return render_template('list_user.html', users=users)

def add_user(info):
    user.insert_user(user.User(0, info['username'], info['phone']))


def search_user(info):
    users = user.search_user(info['username'])

    return render_template('list_user.html', users=users)

def delete_user(info):
    user.delete_user(info)