class Order(object):
    orderID = ''
    email = ''
    # Create contructor

    def __init__(self, orderID, email):
        self.orderID = orderID
        self.email = email

    def __repr__(self):
        return str(self)


# def makeOrder(orderID, email):
#         order = Order(orderID, email)
#         return order
