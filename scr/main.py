from flask import Flask, render_template
from settings import HOST, PORT, DEBUG

# import blueprint criado
from mod_funcionario.funcionario import bp_funcionario
from mod_clientes.cliente import bp_cliente
from mod_index.index import bp_index
from mod_produto.produto import bp_produto


app = Flask(__name__)

# registro das rotas do blueprint
app.register_blueprint(bp_funcionario)
app.register_blueprint(bp_produto)
app.register_blueprint(bp_cliente)
app.register_blueprint(bp_index)

''' chamadas dos formulários '''
@app.route('/')
def formIndex():
    return render_template('formIndex.html'), 200

@app.route('/funcionario/')
def formListaFuncionario():
    return render_template('formListaFuncionarios.html'), 200

@app.route('/cliente/')
def formListaCliente():
    return render_template('formListaCliente.html'), 200

@app.route('/produto/')
def formListaProduto():
    return render_template('formListaProduto.html'), 200

if __name__ == "__main__":
    """ Inicia o aplicativo WEB Flask """
    app.run(host=HOST, port=PORT, debug=DEBUG)

