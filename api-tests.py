from app import app, db, Cards
import unittest
import json

def test_GetCardInfo():
    response = app.test_client().get('/api/v1/cards/1') #TODO create temperary record to enure test coverage

    assert response.status_code == 200
def test_GetCardDoesNotExist():
    response = app.test_client().get('/api/v1/cards/9999')

    assert response.status_code == 404
def test_GetCardBadInput():
    response = app.test_client().get('/api/v1/cards/one')

    assert response.status_code == 404

def test_PostCardInfo():
    response = app.test_client().post(
    '/api/v1/cards',
    data=json.dumps({
        "name": "guildpact informant",
        "type": "creature",
        "color": "blue",
        "cost": 3,
        "rarity": "common"
                    }),
    content_type='application/json',
    )

    assert response.status_code == 201
def test_PostCardMissingField():
    response = app.test_client().post(
    '/api/v1/cards',
    data=json.dumps({
        "name":"guildpact informant",
            "type": "creature",
            "color": "blue",
            "cost": 3,
            "rarity": "common"
            }),
    content_type='application/json',
    )

    assert response.status_code == 201
def test_PostCardBadInput():
    response = app.test_client().post(
    '/api/v1/cards',
    data=json.dumps({
        "name":"guildpact informant",
            "type": "creature",
            "color": "blue",
            "cost": 3,
            "rarity": "common"
            }),
    content_type='application/json',
    )

    assert response.status_code == 201
