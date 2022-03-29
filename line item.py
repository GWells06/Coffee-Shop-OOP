class LineItem(object):

    def __init__(self, product, amount):
        self._lineitem = LineItem
        if amount > 0:
            self._amount = amount
        else:
            raise ValueError("Amount must be greater than zero")

    def __str__(self):
        return f"{self._product.name:30s}{self._product.price:0.2f}\lb"