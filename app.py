from flask import Flask, request, jsonify, abort, make_response
from flask_sqlalchemy import SQLAlchemy
import json
import os

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(APP_ROOT,"database.db")
db = SQLAlchemy(app)




class Cards(db.Model):
    __tablename__ = 'cards'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Text)
    type = db.Column('type', db.Text)
    color = db.Column('color', db.Text)
    cost = db.Column('cost', db.Text)
    rarity = db.Column('rarity', db.Text)

    # def __init__(self, id, name):
    #     self.id = id
    #     self.name = name

@app.route('/api/v1/cards/<int:card_id>', methods=['GET'])
def get_card(card_id):
    card = Cards.query.get(card_id)
    if not card:
        app.logger.error('card could not be found')
        abort(404)
    return jsonify({'id': card.id,"name":card.name})

@app.route('/api/v1/cards', methods=['POST'])
def add_card():
    if not request.json or not 'name' in request.json:
        abort(400)
    card = Cards(name = request.json['name'], type = request.json['type'], color = request.json['color'], cost = request.json['cost'], rarity = request.json['rarity'])
    db.session.add(card)
    db.session.commit()
    if not card.id:
        app.logger.error('card not saved in db')
        abort(400)
    app.logger.info('card saved')
    return jsonify({'id': card.id,"name":card.name}), 201
   
if __name__ == '__main__':
    app.run(debug=True, 
         port=8080, 
         threaded=True)