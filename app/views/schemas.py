from flask_restx import fields

from app.app import namespace

order_item = namespace.model('OrderItem', {
    'product': fields.String(required=True),
    'quantity': fields.Integer(default=1, min=1, example=1),
    'size': fields.String(required=True, enum=['small', 'medium', 'big']),
})


order_model = namespace.model('Order', {
    'created': fields.Integer(readonly=True),
    'id': fields.String(format='uuid', readonly=True),
    'order': fields.List(fields.Nested(order_item), required=True),
    'status': fields.String(
        readonly=True, enum=['active', 'completed', 'cancelled']
    ),
})
