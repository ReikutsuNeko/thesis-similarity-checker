import functools

from os import (
    path, mkdir
)

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('home', __name__, url_prefix='/')

ALLOWED_EXTENSIONS = ['docx']

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@bp.route('/home', methods=['GET'])
def index():
    return render_template('base.html')

@bp.route('/upload1', methods=['POST'])
def uploadDocForSimBetweenDoc():
    error = None
    files = request.files['check1_files']

    if files and allowed_file(files.filename):
        folderPath = ""

        if session.get('user_id') is not None:
            folderPath = 'upload_personal/'+session.get('user_id')
        else:
            folderPath = 'upload_personal/'+session.get('randId')

        if path.exists(folderPath) is True:
            print(files.filename)
            files.save(folderPath+'/'+files.filename)
        else:
            mkdir(folderPath)
            files.save(folderPath+'/'+files.filename)

    return jsonify(status="failed", error=error)

@bp.route('/upload2', methods=['POST'])
def uploadDocForSimBetweenDb():
    error = None
    files = request.files['check2_files']

    if files and allowed_file(files.filename):
        folderPath = ""

        if session.get('user_id') is not None:
            folderPath = 'upload/'+session.get('user_id')
        else:
            folderPath = 'upload/'+session.get('randId')

        if path.exists(folderPath) is True:
            print(files.filename)
            files.save(folderPath+'/'+files.filename)
        else:
            mkdir(folderPath)
            files.save(folderPath+'/'+files.filename)

    return jsonify(status="failed", error=error)

@bp.route('/check1', methods=['POST'])
def checkSimBetweenDoc():
    error = None
    return jsonify(status="failed", error=error)

@bp.route('/check2', methods=['POST'])
def checkSimWithDb():
    error = None
    return jsonify(status="failed", error=error)