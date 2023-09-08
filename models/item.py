from db import db


class ItemModel(db.Model):
    __table__name = "items"
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),unique=True,nullable=False)
    price = db.Column(db.Float(precision=2),unique=False,nullable=False)
    stor_id = db.Column(db.Integer,unique=False,nullable=False)
    
    