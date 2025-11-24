from .database import db
from datetime import datetime

class User(db.Model):
    __tablename__= "users"
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80), unique=True, nullable=False)
    password=db.Column(db.String(120), nullable=False)
    pincode=db.Column(db.String(10), nullable=False)
    fullname=db.Column(db.String(120), nullable=False)
    role=db.Column(db.String(50), nullable=False,default='user')

class Parking_Lot(db.Model):
    __tablename__='parking_lots'
    id = db.Column(db.Integer,primary_key=True,nullable=False,autoincrement=True)
    prime_loc_name = db.Column(db.String,nullable=False,unique=True)
    price = db.Column(db.Integer,nullable=False)
    address = db.Column(db.String,nullable=False)
    pin_code = db.Column(db.Integer,nullable=False)
    max_spots = db.Column(db.Integer,nullable=False)
    parking_spots=db.relationship('Parking_Spot',cascade='all ,delete-orphan',backref='parking_lot')

class Parking_Spot(db.Model):
    __tablename__='parking_spots'
    id = db.Column(db.Integer,primary_key=True,nullable=False,autoincrement=True)
    lot_id = db.Column(db.Integer,db.ForeignKey("parking_lots.id"),nullable=False)
    status = db.Column(db.String,nullable=False)

class Reserve_Parking_Spot(db.Model):
    __tablename__='reserve_parking_spots'
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    lot_name=db.Column(db.String,db.ForeignKey("parking_lots.prime_loc_name"),nullable=False)
    spot_id = db.Column(db.Integer,db.ForeignKey("parking_spots.id"),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    parking_time_stamp = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    leaving_time_stamp = db.Column(db.DateTime)
    parking_cost = db.Column(db.Integer)
    vehicle_number=db.Column(db.String,nullable=False)
