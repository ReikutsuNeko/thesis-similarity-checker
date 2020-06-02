import functools
import core.main as core_main
import core.gensim_util as gensim_core
import shutil

from os import (
    path, mkdir
)

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('check', __name__, url_prefix='/')

@bp.route('/trainCheck1', methods=['POST'])
def trainPersonalDocument():
    error = None
    folderPath = ""
    modelPath = ""

    if session.get('user_id') is not None:
        folderPath = 'upload_personal/temp_train/'+str(session.get('user_id'))
        modelPath = 'dataset/temporary/'+str(session.get('user_id'))
    else:
        folderPath = 'upload_personal/temp_train/'+session.get('randId')
        modelPath = 'dataset/temporary/'+session.get('randId')

    if path.exists(folderPath) is True:
        listOfDoc = core_main.read_document(folderPath)
        
        if len(listOfDoc) < 2:
            error = "You have to upload 2 or more files"
            return jsonify(status="failed", error=error), 500

        if path.exists(modelPath) is True:
            model = core_main.train_document(listOfDoc, saveModel=True, saveModelDir=modelPath+'/', fileName="default.model")
        else:
            mkdir(modelPath)
            model = core_main.train_document(listOfDoc, saveModel=True, saveModelDir=modelPath+'/', fileName="default.model")

        shutil.rmtree(folderPath)

        return jsonify(status="success")
    else:
        error = "Please upload your files first"

    return jsonify(status="failed",error=error), 500

@bp.route('/check1', methods=['POST'])
def checkSimBetweenDoc():
    error = None
    folderPath = ""
    modelPath = ""
    finalResult = {}
    suspectTemp = {}

    if session.get('user_id') is not None:
        folderPath = 'upload_personal/'+str(session.get('user_id'))
        modelPath = 'dataset/temporary/'+str(session.get('user_id'))
    else:
        folderPath = 'upload_personal/'+session.get('randId')
        modelPath = 'dataset/temporary/'+session.get('randId')

    if path.exists(modelPath+'/default.model') is True:
        if path.exists(folderPath) is True:
            listOfDoc = core_main.read_document(folderPath)
            model = gensim_core.load_model(modelPath, "/default.model")
            infer_vec = core_main.infer_vectors_between_document(model, listOfDoc)
            result = core_main.find_similarities_between_doc_and_dataset(model, infer_vec, len(model.docvecs))

            for docName, listRes in result.items():
                for suspectDoc, acc in listRes:
                    suspectTemp[suspectDoc] = acc*100
                finalResult[docName] = sorted(suspectTemp.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
                suspectTemp = {}

            shutil.rmtree(folderPath)
            shutil.rmtree(modelPath)

            return jsonify(status="success", result=finalResult)
        else:
            error = "Please upload your files first"
    else:
        error = "Please train your document first"

    return jsonify(status="failed", error=error)

@bp.route('/check2', methods=['POST'])
def checkSimWithDb():
    error = None
    folderPath = ""
    finalResult = {}
    suspectTemp = {}

    if session.get('user_id') is not None:
        folderPath = 'upload/'+str(session.get('user_id'))
    else:
        folderPath = 'upload/'+session.get('randId')

    if path.exists(folderPath) is True:
        listOfDoc = core_main.read_document(folderPath)
        model = gensim_core.load_model("dataset/main/", "default.model")
        infer_vec = core_main.infer_vectors_between_document(model, listOfDoc)
        result = core_main.find_similarities_between_doc_and_dataset(model, infer_vec)
        
        for docName, listRes in result.items():
            for suspectDoc, acc in listRes:
                suspectTemp[suspectDoc] = acc*100
            finalResult[docName] = sorted(suspectTemp.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
            suspectTemp = {}

        shutil.rmtree(folderPath)

        return jsonify(status="success", result=finalResult)
    else:
        error = "Please upload your files first"

    return jsonify(status="failed", error=error)