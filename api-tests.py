from app import app, db, Cards
import json

#TODO restructure to use JSON schema files for testing
card_id = 0

#POST Request tests
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

    json_data = json.loads(response.data)
    global card_id 
    card_id = json_data['card']['id']

    assert response.status_code == 201
    assert 'card' in json_data
    assert 'code' in json_data
    assert 'id' in json_data['card']
    assert 'name' in json_data['card']
    assert 'color' in json_data['card']
    assert 'cost' in json_data['card']
    assert 'type' in json_data['card']
    assert 'rarity' in json_data['card']

def test_PostCardMissingField():
    response = app.test_client().post(
    '/api/v1/cards',
    data=json.dumps({
        "name":"guildpact informant",
            "type": "creature",
            "cost": 3,
            "rarity": "common"
            }),
    content_type='application/json',
    )
    json_data = json.loads(response.data)

    assert response.status_code == 400
    assert 'error' in json_data
    assert 'code' in json_data['error']
    assert 'message' in json_data['error']

def test_PostCardBadInput():
    response = app.test_client().post(
    '/api/v1/cards',
    data=json.dumps({
        "name":"guildpact informant",
            "type": "creature",
            "color": {"blue": "error"},
            "cost": 3,
            "rarity": "common"
            }),
    content_type='application/json',
    )
    json_data = json.loads(response.data)

    assert response.status_code == 400
    assert 'error' in json_data
    assert 'code' in json_data['error']
    assert 'message' in json_data['error']

#GET Request tests
def test_GetCardInfo():
    global card_id
    response = app.test_client().get('/api/v1/cards/' + str(card_id))
    json_data = json.loads(response.data)

    assert response.status_code == 200
    assert 'card' in json_data
    assert 'code' in json_data
    assert 'id' in json_data['card']
    assert 'name' in json_data['card']
    assert 'color' in json_data['card']
    assert 'cost' in json_data['card']
    assert 'type' in json_data['card']
    assert 'rarity' in json_data['card']

def test_GetCardDoesNotExist():
    response = app.test_client().get('/api/v1/cards/9999')
    json_data = json.loads(response.data)

    assert response.status_code == 404
    assert 'error' in json_data
    assert 'code' in json_data['error']
    assert 'message' in json_data['error']

def test_GetCardBadInput():
    response = app.test_client().get('/api/v1/cards/one')

    assert response.status_code == 404


    

#PUT Request test
def test_PutCardInfo():
    global card_id
    response = app.test_client().put(
    '/api/v1/cards/' + str(card_id),
    data=json.dumps({
        "name": "guildpact informant",
        "type": "creature",
        "color": "blue",
        "cost": 3,
        "rarity": "common"
                    }),
    content_type='application/json',
    )

    json_data = json.loads(response.data)

    assert response.status_code == 200
    assert 'card' in json_data
    assert 'code' in json_data
    assert 'id' in json_data['card']
    assert 'name' in json_data['card']
    assert 'color' in json_data['card']
    assert 'cost' in json_data['card']
    assert 'type' in json_data['card']
    assert 'rarity' in json_data['card']

#DELETE Request test
def test_DeleteCardInfo():
    global card_id
    response = app.test_client().delete(
    '/api/v1/cards/' + str(card_id),
    data=json.dumps({
        "name": "guildpact informant",
        "type": "creature",
        "color": "blue",
        "cost": 3,
        "rarity": "common"
                    }),
    content_type='application/json',
    )

    json_data = json.loads(response.data)

    assert response.status_code == 200
    assert 'card' in json_data
    assert 'code' in json_data
    assert 'id' in json_data['card']
    assert 'name' in json_data['card']
