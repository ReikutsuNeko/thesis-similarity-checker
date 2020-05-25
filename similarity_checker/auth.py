from app import db

from models import User
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        error = None

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        password_confirmation = request.form['password_confirmation']

        if not name:
            error = 'Username required.'
        elif not email:
            error = 'Email required'
        elif not password:
            error = 'Password required.'
        elif not password_confirmation:
            error = 'You need to confirm your password'
        elif password != password_confirmation:
            error = "Password didn't match"

        if error is None:
            user = User(name=name, email=email, password=generate_password_hash(password, method='pbkdf2:sha256', salt_length=8))
            db.session.add(user)
            db.session.commit()
            session['user_id'] = user.id
            return jsonify(status="success", url="/")

        return jsonify(status="failed", error= error)

@bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        print("masuk")
        error = None

        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user is None:
            error = "User not exists, Please register first"
        else:
            if check_password_hash(user.password, password) is True:
                session['user_id'] = user.id
                return jsonify(status="success", url="/")
            else:
                error = "Password not match"

        return jsonify(status="failed", error= error)

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# @bp.before_app_request
# def load_logged_in_user():
#     user = session.get('user_id')

#     if user is None:
#         print('No User are logged in')
#     else:
#         print("User %s logged in".format(user))

# def login_required(view):
#     @functools.wraps(view)
#     def wrapped_view(**kwargs):
#         if g.user is None:
#             return redirect(url_for('auth.login'))

#         return view(**kwargs)

#     return wrapped_view