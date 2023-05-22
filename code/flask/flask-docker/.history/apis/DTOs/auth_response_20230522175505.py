
@dataclass
class Auth:
    token: str

    def __init__(self, user_name="", password=""):
        self.user_name = user_name
        self.password = password

    def __str__(self):
        return self.dumps(dict(self), ensure_ascii=False)

    def __to_json(self):
        return self.__str__()
