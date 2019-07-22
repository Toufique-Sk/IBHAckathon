

from flask import Blueprint
shopController = Blueprint('shopController','projectrepair')


from .. import model
shop=model.Shop()
# a simple page that says hello
    
    
@shopController.route('/getAll')
def getAll():
    return shop.selectAll()

@shopController.route('/hello')
def hello():
    return "Hello guyzzz"