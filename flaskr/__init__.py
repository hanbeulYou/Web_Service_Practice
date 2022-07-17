from crypt import methods
import os

from flask import Flask, redirect, render_template, request, redirect, url_for
from . import db, book, user

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    # book list 보이기
    @app.route('/')
    def list_book():
        return book.list_book()

    # book search
    @app.route('/', methods=['POST'])
    def search_book():
        if request.form['title'] == 'all' :
            return book.list_book()
        else :
            return book.search_book(request.form)

    # book delete
    @app.route('/deletebook', methods=['POST'])
    def delete_book():
        book.delete_book(request.form.getlist('id'))
        return redirect('/')

    # book add
    @app.route('/addbook', methods=["GET"])
    def add_book():
        return render_template('add_book.html')

    # book add endpoint
    @app.route('/addbook', methods=["POST"])
    def add_book_post():
        book.add_book(request.form)
        return redirect('/')


    # user list 보이기
    @app.route('/users')
    def list_user():
        return user.list_user()

    # user search
    @app.route('/users', methods=['POST'])
    def search_user():
        if request.form['username'] == 'all' :
            return user.list_user()
        else :
            return user.search_user(request.form)

    # user delete
    @app.route('/deleteuser', methods=['POST'])
    def delete_user():
        user.delete_user(request.form.getlist('id'))
        return redirect('/users')

    @app.route('/adduser', methods=['GET'])
    def users():
        return render_template('add_user.html')
    
    @app.route('/adduser', methods=['POST'])
    def users_add():
        user.add_user(request.form)
        return redirect('/users')

    @app.route('/borrowbook', methods=['POST'])
    def borrow_bood():
        print(request.form['user_id'])
        print(request.form.getlist('ids'))
        return redirect('/')


    return app