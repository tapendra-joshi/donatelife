import datetime
from models.database import IndexedTimestampModel,db,Column,Model
from constants.user_constants import IndianStates
from sqlalchemy_utils import ChoiceType
import json

class BloodBankModel(IndexedTimestampModel):
    __tablename__ = "blood_banks"
    
    id = Column(db.BigInteger,primary_key=True,autoincrement=True,nullable=False)
    name = db.Column(db.String(255),nullable=False)
    email = db.Column(db.String(255),unique=True)
    address = db.Column(db.String(255),nullable=False)
    state = db.Column(ChoiceType(IndianStates), nullable=False,index=True)
    country = db.Column(db.String(65),nullable=False,default="India",index=True)
    blood_stock_id = db.Column(db.BigInteger,db.ForeignKey('blood_stock.id'))

    def __init__(self,name,email,state,country,address,blood_stock_id):
        
        self.email = email
        self.name = name
        self.address = address
        self.state = state
        self.country = country
        self.blood_stock_id = blood_stock_id

    def to_json(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "email" : self.email,
            "address" : self.address,
            "state" : self.state,
            "country" : self.country,
            "blood_stock" : {
                "ab_positive":self.blood_stock_id.ab_positive,
                "ab_negative":self.blood_stock_id.ab_negative,
                "a_positive":self.blood_stock_id.a_positive,
                "a_negative":self.blood_stock_id.a_negative,
                "b_positive":self.blood_stock_id.b_positive,
                "o_positive":self.blood_stock_id.o_positive,
                "o_negative":self.blood_stock_id.o_negative
            }
        }


class BloodStock(Model):
    __tablename__="blood_stock"

    id = Column(db.BigInteger,primary_key=True,autoincrement=True,nullable=False)
    ab_positive = db.Column(db.BigInteger,default=0,nullable=False,index=True)
    ab_negative = db.Column(db.BigInteger,default=0,nullable=False,index=True)
    a_positive = db.Column(db.BigInteger,default=0,nullable=False,index=True)
    a_negative = db.Column(db.BigInteger,default=0,nullable=False,index=True)
    b_positive = db.Column(db.BigInteger,default=0,nullable=False,index=True)
    b_negative = db.Column(db.BigInteger,default=0,nullable=False,index=True)
    o_positive = db.Column(db.BigInteger,default=0,nullable=False,index=True)
    o_negative = db.Column(db.BigInteger,default=0,nullable=False,index=True)

    blood_bank_stock_rel = db.relationship('BloodBankModel',backref='BloodStock')
