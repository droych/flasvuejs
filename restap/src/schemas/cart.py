from src.common import db, ma


class CartSchema(ma.Schema):
    class Meta:
        fields = ("UserId", "quantity", "productIdr")


cart_schema = CartSchema()
carts_schema = CartSchema(many=True)