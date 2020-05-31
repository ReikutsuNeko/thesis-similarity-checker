from app import db
from sqlalchemy import desc

from models import User
from models import HistoryHeader
from models import HistoryDetail
import functools
import uuid

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('history', __name__, url_prefix='/')

@bp.route('/saveSessionTable1', methods=['POST'])
def saveTable1Data():
    jsonData = request.get_json(force=True)

    header = jsonData['header']
    data = jsonData['data']

    if session.get('check1') is None:
        session['check1'] = jsonData
    else:
        session['check1'] = jsonData

    return jsonify(status="success")

@bp.route('/saveTable1ToDb', methods=['POST'])
def saveTable1ToDb():
    error = None

    jsonData = session.get('check1')
    header = ""
    data = ""

    if jsonData is None:
        error = "Something went wrong"
        return jsonify(status="failed", error=error)
    else:
        header = jsonData['header']
        data = jsonData['data']
    
    if session.get('user_id') is not None:
        headerDb = HistoryHeader(user_id=session.get('user_id'))
        db.session.add(headerDb)
        db.session.commit()
        headerDb = HistoryHeader.query.filter_by(user_id=session.get('user_id')).order_by(desc(HistoryHeader.id)).first()

        detailDb = HistoryDetail(header_id=headerDb.id,detail_type=header,list_detail=data)
        db.session.add(detailDb)
        db.session.commit()

        return jsonify(status="success",data=detailDb.id)
    else:
        error = "You're not authenticated to access this page"

    return jsonify(status="failed", error=error)

@bp.route('/saveSessionTable2', methods=['POST'])
def saveTable2Data():
    jsonData = request.get_json(force=True)

    header = jsonData['header']
    data = jsonData['data']

    if session.get('check2') is None:
        session['check2'] = jsonData
    else:
        session['check2'] = jsonData

    return jsonify(status="success")

@bp.route('/saveTable2ToDb', methods=['POST'])
def saveTable2ToDb():
    error = None

    jsonData = session.get('check2')
    header = ""
    data = ""

    if jsonData is None:
        error = "Something went wrong"
        return jsonify(status="failed", error=error)
    else:
        header = jsonData['header']
        data = jsonData['data']
    
    if session.get('user_id') is not None:
        headerDb = HistoryHeader(user_id=session.get('user_id'))
        db.session.add(headerDb)
        db.session.commit()
        headerDb = HistoryHeader.query.filter_by(user_id=session.get('user_id')).order_by(desc(HistoryHeader.id)).first()

        detailDb = HistoryDetail(header_id=headerDb.id,detail_type=header,list_detail=data)
        db.session.add(detailDb)
        db.session.commit()

        return jsonify(status="success",data=detailDb.id)
    else:
        error = "You're not authenticated to access this page"

    return jsonify(status="failed", error=error)

@bp.route('/getHistory', methods=['POST'])
def getHistory():
    error = None

    historyData = {}
    detailTemp = []
    headerData = HistoryHeader.query.filter_by(user_id=session.get('user_id')).all()

    if headerData is None:
        error = "No History"
    else:
        for data in headerData:
            detailDatas = HistoryDetail.query.filter_by(header_id=data.id)
            for detailData in detailDatas:
                tblData = detailData.detail_type+""+detailData.list_detail
                detailTemp.append(tblData)
            historyData[str(data.created_at.strftime("%d %B, %Y %H:%M"))] = detailTemp
            detailTemp = []
        
        return jsonify(status="success", result=historyData)

    return jsonify(status="failed", error=error)