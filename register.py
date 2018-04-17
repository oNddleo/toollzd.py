class Register(object):
    password = ''
    email = ''
    name = ''
    # Create contructor

    def __init__(self, email, password, name):
        self.password = password
        self.email = email
        self.name = name

    def __repr__(self):
        return str(self)
