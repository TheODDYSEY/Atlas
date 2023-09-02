import uuid
from flask import Flask,request
from flask_smorest import abort
from db import items,stores

app = Flask(__name__)




# JSON is just a long string that follows a specific format like the one above 
#  a python dictionary is returned as a JSON

# NEW FUNCTION
@app.get("/store")  # GET http://127.0.0.1:5005/store

def get_stores():
    return {"stores":list(stores.values())}


# NEW FUNCTION
@app.post("/store") #POST http://127.0.0.1:5005/store
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return store

# NEW FUNCTION
# create stores and items
@app.post("/item") #POST http://127.0.0.1:5005/store/My Store/item
def create_item(name):
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        abort (404,message="Store not found")
    
    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item

    return item ,201


# gets all items 
@app.get("/item")
def get_all_items():
    return {"items":list(items.values())}


# NEW FUNCTION
# new function 
@app.get("/store/<string:store_id>") #GET http://127.0.0.1:5005/store/My Store
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404,message="Store not found")


# NEW FUNCTION
# return items from a store in aas a dict 
@app.get("/item/<string:item_id>") #GET http://127.0.0.1:5005/store/My Store/item
def get_item(item_id):
    try:
        return items[item_id]
    except:
        KeyError
    abort(404,message="Item not found")






# OLD FUNCTION
# @app.get("/store")  # GET http://127.0.0.1:5005/store

# def get_stores():
#     return {"stores":stores}
#



# OLD FUNCTION
# # create stores 
# @app.post("/store") #POST http://127.0.0.1:5005/store
# def create_store():
#     request_data = request.get_json()
#     new_store = {"name":request_data["name"],"items":[]}
#     stores.append(new_store)
#     return new_store,201



# # OLD FUNCTION
# # create stores and items
# @app.post("/store/<string:name>/item") #POST http://127.0.0.1:5005/store/My Store/item
# def create_item(name):
#     request_data = request.get_json()
#     for store in stores:
#         if store["name"] == name:
#             new_item = {"name":request_data["name"],"price":request_data["price"]}
#             store["items"].append(new_item)
#             return new_item,201
#     return {"Message":"Store not found"},404    


# OLD FUNCTION
# get specific store name 
# @app.get("/store/<string:name>") #GET http://127.0.0.1:5005/store/My Store
# def get_store(name):
#     for store in stores:
#         if store["name"] == name:
#             return store
#     return  {"message":"Store not found"},404


# # OLD FUNCTION
# # return items from a store in aas a dict 
# @app.get("/item/<string:item_id>") #GET http://127.0.0.1:5005/store/My Store/item
# def get_item_in_store(name):
#     for store in stores:
#         if store["name"] == name:
#             return store["items"]
#     return {"message":"Store not found"},404    
