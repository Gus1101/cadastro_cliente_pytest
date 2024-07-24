from functions.clientes import *
from functions.cadastro_cliente import *

def test_cliente_cadastrado_com_sucesso():
	cliente = Cliente("Augusto",21,"augusto.example@gmaila.com")
	cadastro_cliente = CadastroCliente()
	resposta = cadastro_cliente.cadastrar_cliente(cliente)
	assert resposta == "Cliente cadastrado com sucesso"

def test_cliente_menor_de_idade():
	cliente = Cliente("Augusto",17,"augusto.example@gmaila.com")
	cadastro_cliente = CadastroCliente()
	resposta = cadastro_cliente.cadastrar_cliente(cliente)
	assert resposta == "Cliente menor de idade. Não cadastrado"

def test_cliente_com_nome_invalido():
	cliente = Cliente("Aug",21,"augusto.example@gmaila.com")
	cadastro_cliente = CadastroCliente()
	resposta = cadastro_cliente.cadastrar_cliente(cliente)
	assert resposta == "Cliente com nome invalido. Não cadastrado"

def test_cliente_com_email_invalido():
	cliente = Cliente("Augusto",21,"augusto.examplegmaila.com")
	cadastro_cliente = CadastroCliente()
	resposta = cadastro_cliente.cadastrar_cliente(cliente)
	assert resposta == "Cliente com email invalido. Não cadastrado"
	