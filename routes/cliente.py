from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)

# ROTAS
@cliente_route.route('/') #LISTAR TODOS OS CLIENTES
def lista_clientes():
    return render_template('lista_clientes.html', clientes=CLIENTES)


# INSERINDO UM CLIENTE NO BANCO DE DADOS 
@cliente_route.route('/', methods =['POST']) 
def inserir_cliente():
    data = request.json
    novo_usuario = {
        "id": len(CLIENTES) + 1,
        "nome": data['nome'],
        "email": data['email'],
    }
    CLIENTES.append(novo_usuario)
    return render_template('item_cliente.html', cliente=novo_usuario)


# CADASTRO DE UM NOVO CLIENTE NO BANCO DE DADOS
@cliente_route.route('/new') 
def form_cliente():
    return render_template('form_cliente.html')


#EXIBIR DETALHES DO CLIENTE
@cliente_route.route('/<int:cliente_id>') 
def detalhe_cliente(cliente_id):
    return render_template('detalhe_cliente.html')


#FORMULÁRIO PARA EDITAR UM CLIENTE
@cliente_route.route('/<int:cliente_id>/edit') 
def form_edit_cliente(cliente_id):
    cliente = None
    for c in CLIENTES:
        if c['id'] == cliente_id:
            cliente = c
    return render_template('form_cliente.html', cliente=cliente)


#ATUALIZAR DADOS DO CLIENTE
@cliente_route.route('/<int:cliente_id>/update', methods=['PUT']) 
def atualizar_cliente(cliente_id):
    cliente_editado = None
    data = request.json
    for c in CLIENTES:
        if c['id'] == cliente_id:
            c["nome"] = data["nome"]
            c["email"] = data["email"]
            cliente_editado = c
    return render_template('item_cliente.html', cliente=cliente_editado)


#DELETAR OS REGISTROS DO CLIENTE
@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE']) 
def deletar_cliente(cliente_id):
    global CLIENTES
    CLIENTES = [c for c in CLIENTES if c['id'] != cliente_id]
    return {'ok' : 'ok'}