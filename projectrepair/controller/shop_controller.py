

from flask import Blueprint
shopController = Blueprint('shopController',__name__)


from ..models import shop_model
shop=shop_model.Shop()
# a simple page that says hello
    
    
@shopController.route('/getAll')
def getAll():
    return shop.selectAll()

@shopController.route('/hello')
def hello():
    return "Hello guyzzz"