class User():
    def __init__(self, name, roles):
        self.name = name
        self.roles = roles
        self.data = data

    def __str__(self):
        dict = {"name": self.name, "roles": self.roles}
        return str(dict)

    def __repr__(self):
        return self.__str__()
