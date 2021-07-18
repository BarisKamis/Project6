from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///'+os.path.join(basedir, 'address.sqlite')
app.config['SECRET_KEY']="merhaba"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
  
class Telefonnumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    surname= db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    telefonnumber=db.Column(db.Integer, nullable=False)

db.create_all()

@app.route("/")
def emails():
    contacts = Telefonnumber.query.order_by(Telefonnumber.name.asc())
    return render_template('index.html', contacts=contacts)

@app.route("/search", methods = ['GET', 'POST'])
def search():
    if request.method == "POST":
        search=request.form["search"]
        contacts=Telefonnumber.query.filter_by(name=search).all()
        return render_template('search.html', contacts=contacts)
    else:
        contacts = Telefonnumber.query.order_by(Telefonnumber.name.asc())
        return render_template('index.html', contacts=contacts)

@app.route("/addcontact", methods = ['GET', 'POST'])
def addcontact():
    if request.method == "POST":     
        entry = Telefonnumber(name=request.form["name"], surname=request.form["surname"], email=request.form["email"], telefonnumber=request.form["telefonnumber"])
        db.session.add(entry)
        db.session.commit()
        contacts = Telefonnumber.query.filter_by().all()
        return render_template('index.html', contacts=contacts)
    else:
        return render_template("addcontact.html")

if __name__ =="__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=80)