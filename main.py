from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from env import PRODUCTION_KEY, TEST_KEY
from gamblers import make_gamblers, read_gamblers
import time

app = Flask(__name__)
CORS(app)

cors = CORS(app, resources={
    r"/*": {
        "origins": "*"

    }
})

URL = 'https://api.pagar.me/core/v5/orders'
first_read = True

# headers = {
#     'accept': 'application/json',
#     'authorization': f'Basic {TEST_KEY}',
#     'content-type': 'application/json'
# }
headers = {
    'accept': 'application/json',
    'authorization': f'Basic {PRODUCTION_KEY}',
    'content-type': 'application/json'
}

gamblers_list = []


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World'


@app.route('/credit_card', methods=['POST'])
def credit_payment():
    data = request.json
    response = requests.post(URL, json=data, headers=headers)
    print(response.text)

    return response.json()


@app.route('/pix', methods=['POST'])
def pix_payment():
    data = request.json
    response = requests.post(URL, json=data, headers=headers)
    print(response.text)

    return response.json()


@app.route('/get_charge/<id>', methods=['GET'])
def get_charge(id):
    response = requests.get(
        f'https://api.pagar.me/core/v5/charges/{id}', headers=headers)
    return response.json()


@app.route('/get_gamblers', methods=['GET'])
def get_gamblers():
    global first_read
    if first_read:
        print('first reading')
        make_gamblers(gamblers_list)
        first_read = False
        print('end of reading')
        return jsonify(read_gamblers(gamblers_list))

    return jsonify(read_gamblers(gamblers_list))


if __name__ == "__main__":
    app.run()
