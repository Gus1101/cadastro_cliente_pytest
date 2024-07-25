IDADE_MINIMA = 18
CARACTER_OBRIGATORIO = "@"

class CadastroCliente:
	def __init__(self):
		self.clientes_cadastrados = []

	def cadastrar_cliente(self, cliente):

		if not isinstance(cliente.idade, int):
			return "Cliente com idade invalida. Não cadastrado"

		if cliente.idade < IDADE_MINIMA:
			return "Cliente menor de idade. Não cadastrado"

		if len(cliente.nome) <= 3:
			return "Cliente com nome invalido. Não cadastrado"

		if CARACTER_OBRIGATORIO not in cliente.email:
			return "Cliente com email invalido. Não cadastrado"

		self.clientes_cadastrados.append(cliente)
		return "Cliente cadastrado com sucesso"
