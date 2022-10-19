from src.common import db, ma
#from src.db import model

class CartSchema(ma.Schema):
    class Meta:
        fields = ( "productId","product_name","quantity","image","product_rate","Total")
cart_schema = CartSchema()
carts_schema = CartSchema(many=True)
