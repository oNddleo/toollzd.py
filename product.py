class Product(object):
    name = ''
    oldPrice = ''
    price = ''
    discount = ''
    promo = ''
    delivery_fee = ''

    # Create contructor

    def __init__(self, name, oldPrice, price, discount, promo, delivery_fee):
        self.oldPrice = oldPrice
        self.price = price
        self.name = name
        self.discount = discount
        self.promo = promo
        self.delivery_fee = delivery_fee

    def __repr__(self):
        return str(self)
