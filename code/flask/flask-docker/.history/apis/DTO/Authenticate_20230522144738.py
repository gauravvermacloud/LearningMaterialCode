
from marshmallow_dataclass import dataclass


@dataclass
class Aunthenicate:
    user_name: str
    password: str

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __to_json(self):
        return delf.__str__()

    def from_json(json_dict):
