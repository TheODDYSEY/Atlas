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

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name":request_data["name"],"items":[]}
    stores.append(new_store)
    return new_store,201