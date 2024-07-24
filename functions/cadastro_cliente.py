class CadastroCliente:
	def __init__(self):
		self.clientes_cadastrados = []

	def cadastrar_cliente(self, cliente):

		if cliente.idade < 18:
			return "Cliente menor de idade. Não cadastrado"

		if len(cliente.nome) <= 3:
			return "Cliente com nome invalido. Não cadastrado"

		if "@" not in cliente.email:
			return "Cliente com email invalido. Não cadastrado"

		self.clientes_cadastrados.append(cliente)
		return "Cliente cadastrado com sucesso"
