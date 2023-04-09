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
db_path = "sqlite:///{}".format(os.path.join(project_dir, "accounting.db"))
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# init db object
db = SQLAlchemy(app)
# Marshmallow for converting objects to python dictionaries
ma = Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    transactions = db.relationship('Transaction', backref='user')

    def __repr__(self):
        return '(%s, %s, %s)' % (self.name, self.email, self.password)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    amount_dollars = db.Column(db.Integer)
    amount_cents = db.Column(db.Integer)
    reason = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '(%s, %s, %s, %s, %s)' % (self.user_id, self.date, self.amount_dollars, self.amount_cents, self.reason)
    
class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    name = ma.auto_field()
    email = ma.auto_field()
    password = ma.auto_field()

class transactionsSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Transaction

    user_id = ma.auto_field()
    date = ma.auto_field()
    amount_dollars = ma.auto_field()
    amount_cents = ma.auto_field()
    reason = ma.auto_field()

def populateDB():
    if (User.query.filter_by(name='user').first() is None):
        user1 = User(name='user', email='user@mail.com', password='12345')
        db.session.add(user1)
    if (Transaction.query.filter_by(reason='Testin').first() is None):
        transaction1 = Transaction(user_id=1, date=date.today(), amount_dollars=60, amount_cents=25, reason="Testing")
        db.session.add(transaction1)
    db.session.commit()

@app.route('/', methods=['GET'])
def home():
    return("HOME...")

@app.route('/login', methods=['GET','POST'])
def submit_user():
    if request.method == "POST":
        post_data = request.get_json()
        if (User.query.filter_by(name=post_data['name']).first() is None):
            new_user = User(name=post_data['name'], email=post_data['email'], password=post_data['password'])
            db.session.add(new_user)
            db.session.commit()
    else:
        user_obj = Userdb_to_dict()
    return jsonify(user_obj)

def Userdb_to_dict():
    userTable = User.query.all()
    userSchema = UserSchema(many=True)
    output = userSchema.dump(userTable)
    return output

with app.app_context():
    db.drop_all()
    db.create_all()
    populateDB()

if __name__ == '__main__':
    app.run(debug=True)