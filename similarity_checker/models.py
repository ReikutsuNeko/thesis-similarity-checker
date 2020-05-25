from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(255))

    historyHeaders = db.relationship('HistoryHeader', backref='users', lazy=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def serialize(self):
        return {
            'user_id': self.id,
            'name': self.name,
            'email': self.email
        }

class HistoryHeader(db.Model):
    __tablename__ = 'historyHeaders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    historyDetails = db.relationship('HistoryDetail', backref='historyHeaders', lazy=False)

    def __init__(self, user_id, user):
        self.user_id = user_id

    def serialize(self):
        return {
            'header_id': self.id,
            'user_id': self.user_id,
            'created_at': self.created_at
        }

class HistoryDetail(db.Model):
    __tablename__ = 'historyDetails'

    id = db.Column(db.Integer, primary_key=True)
    header_id = db.Column(db.Integer, db.ForeignKey('historyHeaders.id'))
    detail_type = db.Column(db.String(100))
    suspect_name = db.Column(db.String(100))
    doc_name = db.Column(db.String(100))
    source_name = db.Column(db.String(100))
    percentage = db.Column(db.Integer)

    def serialize(self):
        return {
            'detail_id': self.id,
            'header_id': self.header_id,
            'detail_type': self.detailType,
            'suspect_name': self.suspect_name,
            'doc_name': self.doc_name,
            'source_name': self.source_name,
            'percentage': self.percentage
        }