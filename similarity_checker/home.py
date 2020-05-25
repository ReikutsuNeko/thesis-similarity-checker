import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/home', methods=['GET'])
def index():
    return render_template('base.html')