from flask import Blueprint, render_template, request
import requests
from settings import HEADERS_API, ENDPOINT_PRODUTO
import base64
from mod_produto.GeraPdf import PDF
from flask import send_file
from funcoes import Funcoes


bp_produto = Blueprint('produto', __name__, url_prefix="/produto", template_folder='templates')

''' rotas dos formulários '''
@bp_produto.route('/', methods=['GET', 'POST'])
def formListaProduto():
    try:
        response = requests.get( "http://localhost:8000/produto/" )
        response = requests.get(ENDPOINT_PRODUTO, headers=HEADERS_API)
        result = response.json()

        print (ENDPOINT_PRODUTO)

        if (response.status_code != 200):
            raise Exception(result[0])
        
        return render_template('formListaProduto.html', result=result[0])
    except Exception as e:
        return render_template('formListaProduto.html', msgErro=e.args[0])

@bp_produto.route('/form-produto/', methods=['POST'])
def formProduto():
    return render_template('formProduto.html')

# ''' rotas dos formulários '''
# @bp_produto.route('/produto/')
# def formListaProduto():
#     return render_template('formListaProduto.html'), 200

@bp_produto.route('/insert', methods=['POST'])
def insert():
    try:
        # dados enviados via FORM
        id_produto = request.form['id_produto']
        nome = request.form['nome']
        descricao = request.form['descricao']
        #foto = request.form['foto']
        valor_unitario = request.form['valor_unitario']
        # converte a foto em base64
        foto = "data:" + request.files['foto'].content_type + "base64" + str(base64.b64encode(request.files['foto'].read()), "utf-8")

        # monta o JSON para envio a API
        payload = {'id_produto': id_produto, 'nome': nome, 'descricao': descricao, 'foto': foto, 'valor_unitario': valor_unitario}
        
        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(ENDPOINT_PRODUTO, headers=HEADERS_API, json=payload)
        result = response.json()
        
        return render_template('formListaProduto.html', msg=result[0])
    except Exception as e:
        return render_template('formListaProduto.html', msgErro=e.args[0])
    

@bp_produto.route("/form-edit-produto", methods=['POST'])
def formEditProduto():
    try:
        # ID enviado via FORM
        id_produto = request.form['id']
        # executa o verbo GET da API buscando somente o funcionário selecionado,
        # obtendo o JSON do retorno
        response = requests.get(ENDPOINT_PRODUTO + id_produto, headers=HEADERS_API)
        result = response.json()
        if (response.status_code != 200):
            raise Exception(result[0])
        # renderiza o form passando os dados retornados
        return render_template('formProduto.html', result=result[0])
    except Exception as e:
        return render_template('formListaProduto.html', msgErro=e.args[0]) 
    
@bp_produto.route('/edit', methods=['POST'])
def edit():
    try:
        # dados enviados via FORM
        id_produto = request.form['id_produto']
        nome = request.form['nome']
        descricao = request.form['descricao']
        #foto = request.form['foto']
        valor_unitario = request.form['valor_unitario']
        # converte a foto em base64
        foto = "data:" + request.files['foto'].content_type + "base64" + str(base64.b64encode(request.files['foto'].read()), "utf-8")
        # monta o JSON para envio a API
        payload = {'id_produto': id_produto, 'nome': nome, 'descricao': descricao, 'foto': foto, 'valor_unitario': valor_unitario}
        # executa o verbo PUT da API e armazena seu retorno
        response = requests.put(ENDPOINT_PRODUTO + id_produto, headers=HEADERS_API, json=payload)
        result = response.json()
        if (response.status_code != 200 or result[1] != 200):
            raise Exception(result[0])
        return render_template('funcionario.formListaProduto', msg=result[0])
    except Exception as e:

        return render_template('formListaProduto.html', msgErro=e.args[0])
    
    ''' rotas para PDF '''
from mod_produto.GeraPdf import PDF
from flask import send_file

@bp_produto.route('/pdfTodos', methods=['POST'])
def pdfTodos():
    geraPdf = PDF()
    geraPdf.listaTodos()
    return send_file('pdfProdutos.pdf')