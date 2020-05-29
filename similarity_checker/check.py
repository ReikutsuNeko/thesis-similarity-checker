import functools
import core.main as core_main

from os import (
    path, mkdir
)

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('check', __name__, url_prefix='/')

@bp.route('/check1', methods=['POST'])
def checkSimBetweenDoc():
    error = None
    folderPath = ""
    listOfDoc = {}

    if session.get('user_id') is not None:
        folderPath = 'upload_personal/'+session.get('user_id')
    else:
        folderPath = 'upload_personal/'+session.get('randId')

    if path.exists(folderPath) is True:
        listOfDoc = core_main.read_document(folderPath)
        print(listOfDoc)

        return jsonify(status="success", error=error)
    else:
        error = "Please upload your files first"

    return jsonify(status="failed", error=error)

@bp.route('/check2', methods=['POST'])
def checkSimWithDb():
    error = None
    return jsonify(status="failed", error=error)