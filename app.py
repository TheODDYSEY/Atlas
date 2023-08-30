from flask import Flask,request

app = Flask(__name__)


stores = [
    {
        "name":"My Store",
        "items":[
            {
            "name":"Chair",
            "price": 15.99
            }
        ]
    }
] 

# JSON is just a long string that follows a specific format like the one above 
#  a python dictionary is returned as a JSON

@app.get("/store")  # http://127.0.0.1:5000/store

def get_store():
    return {"stores":stores}
#
# create stores 
@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name":request_data["name"],"items":[]}
    stores.append(new_store)
    return new_store,201

# create stores and items
@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name":request_data["name"],"price":request_data["price"]}
            store["items"].append(new_item)
            return new_item,201
    return {"Message":"Store not found"},404    

# get specific store name 
@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return  {"message":"Store not found"},404

# return items from a store in aas a dict 
@app.get("/store/<string:name>/item")
def get_item_in_stores(name):
    for store in stores:
        if store["name"] == name:
            return {"items":store["items"]}
    return {"message":"Store not found"},404    