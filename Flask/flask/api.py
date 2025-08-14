
##put and delete--httpverb
#working with API's--JSON

from flask import Flask,jsonify,request

app=Flask(__name__)  #create an app

##initial data in my todo list
items=[
    {'id':1,'name':'item1','description':'this is item1'},
    {'id':2,'name':'item2','description':'this is item2'}
]

@app.route('/')
def home():
    return 'welcome to the sample to do list app'

#get retrieve all the items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

#get: retrieve specific item by id
@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({"error": " item not found"})
    return jsonify(items)

#post: we create a new task
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error": " item not found"})
    new_item={
        "id":items[-1]["id"]+1 if items else 1,
        "name":request.json["name"],
        "description":request.json["description"]

    }
    items.append(new_item)
    return jsonify(new_item)



    





if __name__==__main__:
    app.run(debug=True)



