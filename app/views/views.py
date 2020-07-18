from flask_restx import Resource

from app.app import namespace, api
from app.orders.orders import OrdersCollection, Order
from app.views.schemas import order_model


orders_collection = OrdersCollection()


@namespace.route('/orders')
class OrdersAPI(Resource):
    @namespace.marshal_list_with(order_model)
    def get(self):
        return orders_collection.to_list()

    @namespace.expect(order_model, validate=True)
    @namespace.marshal_with(order_model)
    def post(self):
        return Order(api.payload['order'], orders_collection).create(), 201


@namespace.route('/orders/<order_id>')
@namespace.param('order_id', 'The order identifier')
class OrderAPI(Resource):
    @namespace.marshal_with(order_model)
    def get(self, order_id):
        return orders_collection.get(order_id), 200

    @namespace.expect(order_model, validate=True)
    @namespace.marshal_with(order_model)
    def put(self, order_id):
        order = orders_collection.get(order_id['order'])
        return order.update(api.payload), 200

    def delete(self, order_id):
        order = orders_collection.get(order_id)
        order.delete()
        return '', 204


@namespace.route('/orders/<order_id>/cancel')
@namespace.param('order_id', 'The order identifier')
class OrderCancel(Resource):
    @namespace.marshal_with(order_model)
    def post(self, order_id):
        order = orders_collection.get(order_id)
        return order.cancel(), 200


@namespace.route('/orders/<order_id>/pay')
@namespace.param('order_id', 'The order identifier')
class OrderPay(Resource):
    @namespace.marshal_with(order_model)
    def post(self, order_id):
        order = orders_collection.get(order_id)
        return order.pay(), 200
