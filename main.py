from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from env import PRODUCTION_KEY, TEST_KEY

app = Flask(__name__)
CORS(app)

cors = CORS(app, resources={
    r"/*": {
        "origins": "*"

    }
})

URL = 'https://api.pagar.me/core/v5/orders'


headers = {
    'accept': 'application/json',
    'authorization': f'Basic {TEST_KEY}',
    'content-type': 'application/json'
}
# headers = {
#     'accept': 'application/json',
#     'authorization': f'Basic {PRODUCTION_KEY}',
#     'content-type': 'application/json'
# }


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
    print(id)

    response = requests.get(
        f'https://api.pagar.me/core/v5/charges/{id}', headers=headers)
    return response.json()


if __name__ == "__main__":
    app.run()
