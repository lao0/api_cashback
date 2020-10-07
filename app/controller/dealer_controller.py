from typing import Tuple

from app.model.dealer import Dealer
from app.database.sqlite import SqliteConnection
from app.validator.fields_validator import FieldsValidator


class DealerController:

    @staticmethod
    def dealer_register(name: str, cpf: str, email: str, password: str) -> Tuple[bool, dict]:

        with SqliteConnection() as database:

            params = (name, cpf, email, password)
            insert_id, db_message = database.insert(table=Dealer.table, columns=Dealer.colums, params=params)

            if not insert_id:
                return False, db_message

        return True, {"mensagem": "O revendedor foi inserido com sucesso!"}

    @staticmethod
    def dealer_login(email: str, password: str) -> Tuple[bool, dict]:

        with SqliteConnection() as database:

            columns = ('email', 'password')
            params = (email, password)

            result, message = database.select(table=Dealer.table, columns=columns, params=params)

            dealer = result.fetchone() if result else None

            if not dealer:
                return False, message

        return True, message
