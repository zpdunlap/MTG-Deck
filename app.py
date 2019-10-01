from flask import Flask
import flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///C:\\Users\\gdihq\\Desktop\\MTG-Deck\\database.db'
db = SQLAlchemy(app)




class cardsDatabase(db.Model):
    __tablename__ = 'cards'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Text)

    def __init__(self, id, name):
        self.id = id
        self.name = name

   
if __name__ == '__main__':
    app.run(debug=True, 
         port=8080, 
         threaded=True)