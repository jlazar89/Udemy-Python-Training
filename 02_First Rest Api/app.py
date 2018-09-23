from flask import Flask, jsonify, request, render_template


app = Flask(__name__)

stores=[
    {
        'name': 'Amazon',
        'items':[
            {
            'name':'my Item',
            'price':15.96
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')


#Post /store date: {name}
@app.route('/store', methods=['POST'])
def createStore():
    request_data = request.get_json()
    newStore = {
        'name' : request_data['name'],
        'item' : []
    }
    stores.append(newStore)
    return jsonify(newStore)

# get/store/<string:name>
@app.route('/store/<string:name>')
def getStoreName(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found'})

#get store
@app.route('/store')
def getStores():
    return jsonify({'stores':stores})

#post /store/<string:name>/item {name:,price:}
@app.route('/store/<string:name>/item',methods=['POST'])
def createItemInStore(name):
    request_data = request.get_json()
    for store in stores:
        if store['name']== name:
            new_item={
                'name' : request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})


#post /store/<string:name>/item {name:,price:}
@app.route('/store/<string:name>/item')
def getItemInStore(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message','store not found'})

app.run(port=5555)
