import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint,abort

from db import items
from schema import ItemSchema,ItemUpdateSchema


blp = Blueprint("Items",__name__,description="Operations on Items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self,item_id):
        try:
            return items[item_id]
        except:
            KeyError
    abort(404,message="Item not found")
    
    
    def delete(self,item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, message="Item not found.")   
            
    def put(Self,item_id):
        item_data = request.get_json()
    # There's  more validation to do here!
    # Like making sure price is a number, and also both items are optional
    # You should also prevent keys that aren't 'price' or 'name' to be passed
    # Difficult to do with an if statement...
        if "price" not in item_data or "name" not in item_data:
            abort(
                400,
                message="Bad request. Ensure 'price', and 'name' are included in the JSON payload.",
            )
        try:
            item = items[item_id]
            item |= item_data

            return item
        except KeyError:
            abort(404, message="Item not found.")            
            
@blp.route("/item")
class ItemList(MethodView):
    def get(self):
        return {"items":list(items.values())}
    
    @blp.arguments(ItemSchema)
    def post(self):
        item_data = request.get_json()
  
        for item in items.values():
            if (
            item_data["name"] == item["name"]
            and item_data["store_id"] == item["store_id"]
            ):
                abort(400, message=f"Item already exists.")

        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item

        return item,201
                