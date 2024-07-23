from models.db import db

class Equivalence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state_from = db.Column(db.String(2), nullable=False)
    state_to = db.Column(db.String(2), nullable=False)
    code_from = db.Column(db.String(10), nullable=False)
    code_to = db.Column(db.String(10), nullable=False)
