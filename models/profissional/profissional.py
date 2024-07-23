from models.db import db

class Professional(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    attributes = db.relationship('Attribute', backref='professional', lazy=True)