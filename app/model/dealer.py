from .model import Model


class Dealer(Model):

    _table = "Dealer"
    _pk = "id_dealer"

    id_dealer: int = 0
    name: str = ""
    cpf: str = ""
    email: str = ""
    password: str = ""
