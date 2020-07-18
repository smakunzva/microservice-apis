import time
import uuid
from dataclasses import dataclass
from typing import Dict, List

from app.app import api


class OrdersCollection:
    """

    """

    def __init__(self):
        self._collection = []

    def __iter__(self):
        for order in self._collection:
            yield order

    def add(self, order):
        self._collection.append(order)
        return len(self._collection) - 1

    def to_list(self):
        return self._collection

    def get(self, order_id):
        for order in self._collection:
            if order.id == order_id:
                return order
        api.abort(404, f'Order with ID {order_id} not found')

    def delete(self, index):
        self._collection.pop(index)


@dataclass
class OrderItem:
    """

    """

    product: str
    size: str
    quantity: int = 1


class Order:
    """

    """

    def __init__(self, order_items: List[Dict], collection: OrdersCollection):
        self.order = [
            OrderItem(**order_item) for order_item in order_items
        ]
        self._collection = collection

        self.id = None
        self.status = None
        self.created = None
        self.updated = None
        self._collection_index = None

    def create(self):
        self.id = str(uuid.uuid4())
        self.status = 'active'
        self.created = time.time()
        self.updated = time.time()
        self._collection_index = self._collection.add(self)
        return self

    def update(self, order_items: List[Dict]):
        self.order = [
            OrderItem(**order_item) for order_item in order_items
        ]
        self.updated = time.time()
        return self

    def delete(self):
        self._collection.delete(self._collection_index)

    def pay(self):
        self.status = 'completed'
        return self

    def cancel(self):
        self.status = 'cancelled'
        return self
