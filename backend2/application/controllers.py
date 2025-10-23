from flask_jwt_extended import current_user, jwt_required,create_access_token
from flask import current_app as app,request, jsonify, abort
from .models import User
from .database import db

def role_required(role):
    def wrapper(fn):
        @jwt_required()
        def give_access(*args,**kwargs):
            if current_user.role != role:
                return jsonify('Unauthorized'),403
            return fn(*args,**kwargs)
        return give_access
    return wrapper

@app.route('/login',methods=['POST'])
def login():
    username=request.json.get('username',None)
    password=request.json.get('password',None)
    
    user=User.query.filter_by(username=username).one_or_none()
    if not user or not user.password==password:
        return jsonify({"msg":"Bad username or password"}),401
        
    role=user.role
    access_token=create_access_token(identity=user)
    return jsonify(access_token=access_token,role=role)

@app.route('/register',methods=['POST'])
def register():
    username=request.json.get("username",None)
    pincode=request.json.get("pincode",None)
    password=request.json.get("password",None)
    fullname=request.json.get("fullname",None)
    user=User.query.filter_by(username=username).first()

    if user:
        return jsonify("user already exists"),400

    user = User(username=username,password=password,pincode=pincode,fullname=fullname)
    db.session.add(user)
    db.session.commit()
    return jsonify("user added"),200

@app.route('/dashboard')
@jwt_required()
def dashboard():
    if current_user.role == 'admin':
        return "hello admin"
    else:
        return "hello user"