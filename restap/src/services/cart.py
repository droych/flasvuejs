#from src.db.addorders import orders_schema, order_schema
from flask_restful import Resource, request


from src.db.model import Orders, Product, User, OrderItems, Cart
from src.schemas.cart import carts_schema,cart_schema
from flask import make_response, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from src.common.base import db
from src.decor.admindec import admin_required
from src.decor.userdec import user_required


class CartListResource(Resource):

    @jwt_required()
    @admin_required([1])
    def get(self):
        order = Orders.query.all()
        return carts_schema.dump(order)

    @jwt_required()
    @user_required([0])
    def post(self,**kwargs):
        user = get_jwt_identity()
        print(user)
        _product_id = request.json['product_id']
        quantity= request.json['quantity']
        purchased = {}
        _cart_total = 0
        _product = Product.query.filter_by(id=_product_id).first()
        _user = User.query.filter_by(email=user).first()
        _user = _user.id
        print(_product.quantity)
        print(quantity)

        if _product.quantity < quantity:
            response = jsonify("Sufficient product Count does not exist")
            return response
        else:
            _cart_total += (_product.product_rate * quantity)
            _product.quantity = _product.quantity - quantity
            db.session.merge(_product)
            db.session.commit()
            purchased.update({id: "added"})
        newoders = Cart(UserId = _user,productId =_product_id,Total=_cart_total,quantity = quantity)
        print(newoders)
        db.session.add(newoders)
        db.session.commit()
        print(newoders)
        user = User.query.filter_by(email=get_jwt_identity()).first()
        with db.session.no_autoflush:
           user.cartitem.append(newoders)
           db.session.add(user)
           db.session.commit()
        response = jsonify("added to cart", {"cart total":_cart_total})
        return response



class CartResource(Resource):
    @jwt_required()
    @user_required([0])
    def get(self, id):
        order_select = Orders.query.get_or_404(id)
        return cart_schema.dump(order_select)

    @jwt_required()
    @admin_required([1])
    def put(self, id):
        order_item = Cart.query.get(id)
        _quantity = request.json['quantity']
        order_item.quantity = _quantity
        db.session.add(order_item)
        db.session.commit()
 
        return cart_schema.dump(order_item)


    @jwt_required()
    @admin_required([1])
    def delete(self, id):
        orders = Cart.query.get_or_404(id)
        db.session.delete(orders)
        db.session.commit()
        return '', 204
