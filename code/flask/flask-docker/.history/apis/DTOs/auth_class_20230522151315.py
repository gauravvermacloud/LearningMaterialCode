from marshmallow_dataclass import dataclass


@dataclass
class Auth:
    user_name: str
    password: str

    def __init__(self):
        pass

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def __str__(self):
        return self.dumps(dict(self), ensure_ascii=False)

    def __to_json(self):
        return self.__str__()

    def from_json(json_dict):
        return Authenticate().Schema().load(json_dict)
