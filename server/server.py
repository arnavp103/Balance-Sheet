import os
from datetime import date, timedelta
from flask import Flask, request, jsonify, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})
# Session init
app.config['SECRET_KEY'] = 'secret213'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes = 10)
app.config['SESSION_TYPE'] = 'filesystem'
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
    date_joined = db.Column(db.Date)
    transactions = db.relationship('Transaction', backref='user')

    def __repr__(self):
        return '(%s, %s, %s, %s)' % (self.name, self.email, self.password, self.date_joined)

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
    date_joined = ma.auto_field()

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
        user1 = User(name='user', email='user@mail.com', password='12345', date_joined=date(2022, 4, 20))
        db.session.add(user1)
    if (Transaction.query.filter_by(reason='Testing').first() is None):
        transaction1 = Transaction(user_id=1, date=date.today(), amount_dollars=60, amount_cents=25, reason="Testing")
        db.session.add(transaction1)
    db.session.commit()

@app.route('/')
def home():
    return("HOME...")

@app.route('/api/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        post_data = request.get_json()
        if (User.query.filter_by(email=post_data['email']).first() is None):
            new_user = User(name=post_data['name'], email=post_data['email'], password=post_data['password'], date_joined=date.today())
            db.session.add(new_user)
            db.session.commit()
        else:
            # TODO: flash error msg
            print("Email already registered")
    return jsonify(Userdb_to_dict())

@app.route('/api/login', methods=['GET','POST'])
def login():
    if session.get('name') is None:
        session['name']= 'Test'
    if request.method == "POST":
        post_data = request.get_json()
        if (User.query.filter_by(email=post_data['email']).first()):
            if (User.query.filter_by(name=post_data['name']).first().password == post_data['password']):
                user = User.query.filter_by(name=post_data['name']).first()
                userSchema = UserSchema(many=False)
                output = userSchema.dump(user)
                session['name'] = output['name']
                return redirect(url_for('success', username=output['name']))
            else:
                # TODO: flash error msg
                print("Incorrect username or password")
    return jsonify(Userdb_to_dict())

@app.route('/success/<username>')
def success(username):
    user = User.query.filter_by(name=username).first()
    userSchema = UserSchema(many=False)
    output = userSchema.dump(user)
    return output

@app.route('/settings/<email>', methods=['GET'])
def user_info(email):
    id = User.query.filter_by(email=email).first().id
    num_days = (date.today() - User.query.filter_by(id=id).first().date_joined).days
    num_transactions = Transaction.query.filter_by(user_id=id).count()
    return jsonify(
        num_days = num_days,
        num_transactions = num_transactions
    )

def Userdb_to_dict():
    userTable = User.query.all()
    userSchema = UserSchema(many=True)
    output = userSchema.dump(userTable)
    return output

with app.app_context():
    try:
        User.query.get(1)
        Transaction.query.get(1)
    except:
        db.create_all()
        populateDB()

if __name__ == '__main__':
    app.run(debug=True)