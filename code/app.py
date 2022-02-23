
from flask import Flask,request
from flask_restful import Resource,Api
from flask_jwt import JWT,jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "jdkdeuilged45dead453dad44d6azddefazedqcfs244"
api = Api(app)
# https://pythonhosted.org/Flask-JWT/
jwt = JWT(app,authenticate,identity) # /auth


items = []

class Item(Resource):
    #@jwt_required()
    def get(self,name):
        item = next(filter(lambda x:x['name'] == name , items), None)
        return {'item':item} ,200 if item is not None else 404

    def post(slef,name):

        if next(filter(lambda x: x['name'] == name ,items),None) is not  None:
            return {'message': 'item Already Exist'},400
        data = request.get_json()
        new_item = {'name':name, 'price':data['price']}
        items.append(new_item)
        return new_item,201

    def delete(self,name):
        global items
        items = list(filter(lambda x:x['name'] != name , items))
        return {'message':'item deleted'}

class ListItem(Resource):
    def get(self):
        return items


api.add_resource(Item,'/item/<string:name>')
api.add_resource(ListItem,'/items')
app.run(debug=True)