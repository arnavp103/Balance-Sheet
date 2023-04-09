import os
from datetime import date
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})
# Setting path to db
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "Users.db"))
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
# app.config['SQLACLHEMY_BINDS'] = {'Users': }
# init db object
db = SQLAlchemy(app)
# Marshmallow for converting objects to python dictionaries
ma = Marshmallow(app)

class Users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return '(%s, %s, %s)' % (self.name, self.email, self.password)

class UsersSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Users

    name = ma.auto_field()
    email = ma.auto_field()
    password = ma.auto_field()

class Transactions(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(Users.id), primary_key=True)
    date = db.Column(db.Date)

    def __repr__(self):
        return '(%s, %s, %s)' % (self.name, self.email, self.password)

class transactionsSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Users

    name = ma.auto_field()
    email = ma.auto_field()
    password = ma.auto_field()

# If db does not exist, create a new one
def init_db():
    try:
        Users.query.get(1)
    except:
        db.create_all()
        user1 = Users(name='user', email='user@mail.com', password='12345')
        db.session.add(user1)
        db.session.commit()

@app.route('/', methods=['GET'])
def home():
    return("HOME...")

@app.route('/login', methods=['GET','POST'])
def submit_user():
    if request.method == "POST":
        post_data = request.get_json()
        if (Users.query.filter_by(name=post_data['name']).first() is None):
            new_user = Users(name=post_data['name'], email=post_data['email'], password=post_data['password'])
            db.session.add(new_user)
            db.session.commit()
    else:
        user_obj = db_to_dict()
    return jsonify(user_obj)

def db_to_dict():
    userTable = Users.query.all()
    userSchema = UsersSchema(many=True)
    output = userSchema.dump(userTable)
    return output

with app.app_context():
    init_db()
    db_to_dict()

if __name__ == '__main__':
    app.run(debug=True)