import os

from flask import Flask
from flask_smorest import Api

from db import db

import models

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.tag import blp as TagBlueprint


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    api = Api(app)

    
    with app.app_context():
        db.create_all()
    
    app.debug = True    

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)

    return app
# import uuid

# from flask_smorest import abort
# from db import items,stores

# # JSON is just a long string that follows a specific format like the one above 
# #  a python dictionary is returned as a JSON

# # NEW FUNCTION
# # get stores
# @app.get("/store")  # GET http://127.0.0.1:5005/store
# def get_stores():
#     return {"stores":list(stores.values())}

# # get store
# @app.get("/store/<string:store_id>") #GET http://127.0.0.1:5005/store/My Store
# def get_store(store_id):
#     try:
#         return stores[store_id]
#     except KeyError:
#         abort(404,message="Store not found")
        
        
# # create store
# @app.post("/store") #POST http://127.0.0.1:5005/store
# def create_store():
#     store_data = request.get_json()
#     if "name" not in store_data:
#         abort(
#             400,
#             message="Bad request. Ensure 'name' is included in the JSON payload.",

#         )
#     for store in stores.values():
#         if store_data["name"] == store["name"]:
#             abort(400,message=f"Store already exists")  
              
#     store_id = uuid.uuid4().hex
#     store = {**store_data, "id": store_id}
#     stores[store_id] = store
#     return store

# # delete store
# @app.delete("/store/<string:store_id>")
# def delete_store(store_id):
#     try:
#         del stores[store_id]
#         return {"message": "Store deleted."}
#     except KeyError:
#         abort(404, message="Store not found.")

# # Get all items
# @app.get("/item")
# def get_all_items():
#     return {"items":list(items.values())}

# # get item
# @app.get("/item/<string:item_id>") #GET http://127.0.0.1:5005/store/My Store/item
# def get_item(item_id):
#     try:
#         return items[item_id]
#     except:
#         KeyError
#     abort(404,message="Item not found")



# # create stores and items
# @app.post("/item") #POST http://127.0.0.1:5005/store/My Store/item
# def create_item():
#     item_data = request.get_json()
#     # Here not only we need to validate data exists,
#     # But also what type of data. Price should be a float,
#     # for example.
#     if (
#         "price" not in item_data
#         or "store_id" not in item_data
#         or "name" not in item_data
#     ):
#         abort(
#             400,
#             message="Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload.",
#         )
#     for item in items.values():
#         if (
#             item_data["name"] == item["name"]
#             and item_data["store_id"] == item["store_id"]
#         ):
#             abort(400, message=f"Item already exists.")

#     item_id = uuid.uuid4().hex
#     item = {**item_data, "id": item_id}
#     items[item_id] = item

#     return item,201


# # delete all items
# @app.delete("/item/<string:item_id>")
# def delete_item(item_id):
#     try:
#         del items[item_id]
#         return {"message": "Item deleted."}
#     except KeyError:
#         abort(404, message="Item not found.")    
    
    
# # update item
# @app.put("/item/<string:item_id>")
# def update_item(item_id):
#     item_data = request.get_json()
#     # There's  more validation to do here!
#     # Like making sure price is a number, and also both items are optional
#     # You should also prevent keys that aren't 'price' or 'name' to be passed
#     # Difficult to do with an if statement...
#     if "price" not in item_data or "name" not in item_data:
#         abort(
#             400,
#             message="Bad request. Ensure 'price', and 'name' are included in the JSON payload.",
#         )
#     try:
#         item = items[item_id]
#         item |= item_data

#         return item
#     except KeyError:
#         abort(404, message="Item not found.")



# # OLD FUNCTION
# # @app.get("/store")  # GET http://127.0.0.1:5005/store

# # def get_stores():
# #     return {"stores":stores}
# #



# # OLD FUNCTION
# # # create stores 
# # @app.post("/store") #POST http://127.0.0.1:5005/store
# # def create_store():
# #     request_data = request.get_json()
# #     new_store = {"name":request_data["name"],"items":[]}
# #     stores.append(new_store)
# #     return new_store,201



# # # OLD FUNCTION
# # # create stores and items
# # @app.post("/store/<string:name>/item") #POST http://127.0.0.1:5005/store/My Store/item
# # def create_item(name):
# #     request_data = request.get_json()
# #     for store in stores:
# #         if store["name"] == name:
# #             new_item = {"name":request_data["name"],"price":request_data["price"]}
# #             store["items"].append(new_item)
# #             return new_item,201
# #     return {"Message":"Store not found"},404    


# # OLD FUNCTION
# # get specific store name 
# # @app.get("/store/<string:name>") #GET http://127.0.0.1:5005/store/My Store
# # def get_store(name):
# #     for store in stores:
# #         if store["name"] == name:
# #             return store
# #     return  {"message":"Store not found"},404


# # # OLD FUNCTION
# # # return items from a store in aas a dict 
# # @app.get("/item/<string:item_id>") #GET http://127.0.0.1:5005/store/My Store/item
# # def get_item_in_store(name):
# #     for store in stores:
# #         if store["name"] == name:
# #             return store["items"]
# #     return {"message":"Store not found"},404    
