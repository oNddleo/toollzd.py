class Login(object):
    password = ''
    email = ''
    # Create contructor

    def __init__(self, email, password):
        self.password = password
        self.email = email
        # self.name = name
        # self.phone = phone
        # self.address = address
    # def __init__(self, email, password, name, phone, address):
    #     self.password = password
    #     self.email = email
    #     self.name = name
    #     self.phone = phone
    #     self.address = address
    def __repr__(self):
        return str(self)