import os
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__, static_folder='../client/dist')

CORS(app, resources={r'/*': {'origins': '*'}})
# Setting path to db
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "Users.db"))
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
# init db object
db = SQLAlchemy(app)

class Users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.Integer)

    def __repr__(self):
        return '<Name %r>' % self.name
    # def __init__(self, name, email, password):
    #     self.name = name
    #     self.email = email
    #     self.password = password

# If db does not exist, create a new one
# def init_db():
#     try:
#         Users.query.get(1)
#     except:
#         db.create_all()
#         user1 = Users(name='admin', email='admin@admin.com', password='adminpw')
#         user2 = Users(name='user', email='user@mail.com', password='userpw')
#         db.session.add(user1)
#         db.session.add(user2)
#         db.session.commit()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

with app.app_context():
    try:
        Users.query.get(1)
    except:
        db.create_all()
        user1 = Users(name='admin', email='admin@admin.com', password='adminpw')
        user2 = Users(name='user', email='user@mail.com', password='userpw')
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

if __name__ == '__main__':
    # init_db()
    app.run(use_reloader=True, port=5000, threaded=True)