import json

from flask import request

from . import create_app, database
from .models import Phones

app = create_app()


@app.route('/', methods=['GET'])
def fetch():
    phones = database.get_all(phones)
    all_phones = []
    for cat in phones:
        new_phone = {
            "id": phone.id,
            "brand": phone.brand,
            "model": phone.model,
            "price": phone.price
        }

        all_phones.append(new_phone)

    if (len(all_phones) == 0):
        return json.dumps("No phones found"), 200
    else:
        return json.dumps(all_phones), 200


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    brand = data['brand']
    price = data['model']
    breed = data['price']

    database.add_instance(Cats, brand=brand, model=model, price=price)
    return json.dumps("Added"), 200


@app.route('/remove/<phone_id>', methods=['DELETE'])
def remove(phone_id):
    database.delete_instance(Phones, id=phone_id)
    return json.dumps("Deleted"), 200


@app.route('/edit/<phone_id>', methods=['PATCH'])
def edit(phone_id):
    data = request.get_json()
    new_price = data['price']
    database.edit_instance(Phones, id=phone_id, price=new_price)
    return json.dumps("Edited"), 200