from flask import Blueprint, render_template, request
import requests
from settings import HEADERS_API, ENDPOINT_CLIENTE
from funcoes import Funcoes


bp_cliente = Blueprint('cliente', __name__, url_prefix="/cliente", template_folder='templates')

''' rotas dos formulários '''
# @bp_cliente.route('/cliente/')
# def formListaCliente():
#     return render_template('formListaCliente.html'), 200

@bp_cliente.route('/', methods=['GET', 'POST'])
def formListaCliente():
    try:
        response = requests.get( "http://localhost:8000/cliente/" )
        response = requests.get(ENDPOINT_CLIENTE, headers=HEADERS_API)
        result = response.json()

        print(ENDPOINT_CLIENTE)

        if (response.status_code != 200):
            raise Exception(result[0])
        
        return render_template('formListaCliente.html', result=result[0])
    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e.args[0])

@bp_cliente.route('/form-cliente/', methods=['POST'])
def formCliente():
    return render_template('formCliente.html')


@bp_cliente.route('/insert', methods=['POST'])
def insert():
    try:
        # dados enviados via FORM
        id_cliente = request.form['id']
        nome = request.form['nome']
        cpf = request.form['cpf']
        senha = Funcoes.cifraSenha(request.form['senha'])
        

        # monta o JSON para envio a API
        payload = {'id_CLIENTE': id_cliente, 'nome': nome, 'cpf': cpf, 'senha': senha}

        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(ENDPOINT_CLIENTE, headers=HEADERS_API, json=payload)
        result = response.json()

        print(result) # [{'msg': 'Cadastrado com sucesso!', 'id': 13}, 200]
        print(response.status_code) # 200

        if (response.status_code != 200 or result[1] != 200):
            raise Exception(result[0])
        
        return render_template('cliente.formListaCliente.html', msg=result[0])

    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e.args[0])