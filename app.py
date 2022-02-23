
from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

stores = [
    {
        "name": "my wonderful store",
        "items": [
            {
                "name": "item 1",
                "price": 47.58
            }
        ]
    },
     {
        "name": "my wonderful store",
        "items": [
            {
                "name": "item 1",
                "price": 47.58
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')
# POST /store data: {name:}
@app.route('/store',methods=['POST'])
def createStor():
    newRequest = request.get_json()
    newStore = {
        'name': newRequest["name"],
        'items':[]
    }
    stores.append(newStore)
    return jsonify(newStore)


# GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def getStoreByName(name):
    
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
        else:
            return jsonify({'message': 'store not exist'})


# GET /store get all stores
@app.route('/store')
def getStore():
    return jsonify({'stores':stores})

# POST /Store create Store
@app.route('/store/<string:name>/item',methods=['POST'])
def createStore(name):
    pass


app.run(port=5000)