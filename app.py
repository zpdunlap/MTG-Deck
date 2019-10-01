from flask import Flask, request, jsonify, abort, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update
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
        return jsonify({'error': {'code': 404, 'message': 'card could not be found'}}), 404
    return jsonify(
    {
    'code': 200,
    'card':
        {
    'id': card.id,
    'name': card.name,
    'color': card.color,
    'cost': card.cost,
    'rarity': card.rarity
        }
    }), 200

@app.route('/api/v1/cards', methods=['POST'])
def add_card():
    fields = ['name', 'type', 'color', 'cost', 'rarity']
    for field in fields:
        if not field in request.json:
         return jsonify({'error': {'code': 400, 'message': "missing '" + field + "' field"}}), 400
    card = Cards(name = request.json['name'], type = request.json['type'], color = request.json['color'], cost = request.json['cost'], rarity = request.json['rarity'])
    db.session.add(card)
    db.session.commit()
    if not card.id:
        app.logger.error('card not saved in db')
        return jsonify({'error': {'code': 400, 'message': 'card not saved in database'}}), 400
    app.logger.info('card saved')
    return jsonify(
    {
    'code': 201,
    'card':
        {
    'id': card.id,
    'name': card.name,
    'color': card.color,
    'cost': card.cost,
    'rarity': card.rarity
        }
    }), 201

@app.route('/api/v1/cards/<int:card_id>', methods=['PUT'])
def update_card(card_id):
    fields = ['name', 'type', 'color', 'cost', 'rarity']
    for field in fields:
        if not field in request.json:
         return jsonify({'error': {'code': 400, 'message': "missing '" + field + "' field"}}), 400
    card = db.session.query(Cards).filter_by(id=card_id)
    if not card:
        app.logger.error('card could not be found')
        return jsonify({'error': {'code': 404, 'message': 'card could not be found'}}), 404
    data_to_update = dict(name = request.json['name'], type = request.json['type'], color = request.json['color'], cost = request.json['cost'], rarity = request.json['rarity'])

    card.update(data_to_update)
    db.session.commit()
    try:
        if not card[0].id:
            app.logger.error('card not saved in db')
            return jsonify({'error': {'code': 400, 'message': 'card not saved in database'}}), 400
    except:
        app.logger.error('card array is empty')
        abort(400)
    app.logger.info('card saved')
    return jsonify(
    {
    'code': 200,
    'card':
        {
    'id': card[0].id,
    'name': card[0].name,
    'color': card[0].color,
    'cost': card[0].cost,
    'rarity': card[0].rarity
        }
    }), 200

@app.route('/api/v1/cards/<int:card_id>', methods=['DELETE'])
def remove_card(card_id):
    card = Cards.query.get(card_id)
    if not card:
        app.logger.error('card could not be found')
        return jsonify({'error': {'code': 404, 'message': 'card could not be found'}}), 404
    db.session.delete(card)
    db.session.commit()
    return jsonify({'code': 200, 'card': {'id': card.id,'name':card.name}}), 200 
   
if __name__ == '__main__':
    app.run(debug=True, 
         port=8080, 
         threaded=True)