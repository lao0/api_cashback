"""Api.

[x] Rota para cadastrar um novo revendedor(a) exigindo no mínimo nome completo, CPF, e- mail e senha;

[x] Rota para validar um login de um revendedor(a);

[x] Rota para cadastrar uma nova compra exigindo no mínimo código, valor, data e CPF do revendedor(a).
    Todos os cadastros são salvos com o status “Em validação” exceto quando o CPF do revendedor(a) for
    153.509.460-56, neste caso o status é salvo como “Aprovado”;

[x] Rota para listar as compras cadastradas retornando código, valor, data, % de cashback aplicado para
    esta compra, valor de cashback para esta compra e status;

[x] Rota para exibir o acumulado de cashback até o momento, essa rota irá consumir essa informação de
    uma API externa disponibilizada pelo Boticário.
"""
from flask import Flask, request
from app import DealerController


app = Flask(__name__)


@app.route("/healthcheck", methods=["GET"])
def health_check():
    """Função para checar a saúde da api."""
    return "OK", 200


@app.route("/revendedor/cadastrar", methods=["POST"])
def dealer_register():
    """Função para cadastrar novo revendedor."""
    body = request.json
    DealerController().dealer_register(name=body.get("nome"),
                                       cpf=body.get("cpf"),
                                       email=body.get("email"),
                                       password=body.get("senha"))
    return "OK", 201


@app.route("/revendedor/login", methods=["POST"])
def dealer_login():
    """Função para logar revendedor."""
    body = request.json
    DealerController().get_dealer(email=body.get("email"), password=body.get("senha"))
    return "OK", 200


@app.route("/compra/cadastrar", methods=["POST"])
def purchase_register():
    """Função para cadastrar nova compra."""
    return "OK", 200


@app.route("/compra/listar", methods=["GET"])
def purchase_list():
    """Função para listar compras."""
    return "OK", 200


@app.route("/cashback", methods=["GET"])
def get_cashback():
    """Função para resgatar quantidade de cashback."""
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
