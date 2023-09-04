import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from db import items


blp = Blueprint("stores",__name__,description="Operations on Items")

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