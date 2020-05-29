from app import db

from models import User
import functools
import uuid

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    error = None
    jsonData = request.get_json(force=True)

    name = jsonData['name']
    email = jsonData['email']
    password = jsonData['password']
    password_confirmation = jsonData['passwordConfirmation']

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

    user = User.query.filter_by(email=email).first()

    if user is not None:
        if user.email == email:
            error = "Email already exists"

    if error is None:
        user = User(name=name, email=email, password=generate_password_hash(password, method='pbkdf2:sha256', salt_length=8))
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user.id
        g.user = User.query.filter_by(email=email).first()
        return jsonify(status="success", error=None)

    return jsonify(status="failed", error=error)

@bp.route('/login', methods=['POST'])
def login():
    error = None
    jsonData = request.get_json(force=True)

    email = jsonData['email']
    password = jsonData['password']

    user = User.query.filter_by(email=email).first()

    if user is None:
        error = "User not exists, Please register first"
    else:
        if check_password_hash(user.password, password) is True:
            session['user_id'] = user.id
            g.user = user
            return jsonify(status="success", error=None)
        else:
            error = "Password not match"

    return jsonify(status="failed", error=error)
        
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@bp.before_app_request
def load_logged_in_user():
    user = session.get('user_id')

    if user is None:
        if session.get('randId') is None:
            randId = str(uuid.uuid4())
            session['randId'] = randId
        else:
            print(session.get('randId'))
        g.user = None
    else:
        g.user = User.query.filter_by(id=session.get('user_id')).first()

# def login_required(view):
#     @functools.wraps(view)
#     def wrapped_view(**kwargs):
#         if g.user is None:
#             return redirect(url_for('auth.login'))

#         return view(**kwargs)

#     return wrapped_view