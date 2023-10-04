from flask import Blueprint, render_template
bp_funcionario = Blueprint('funcionario', __name__, url_prefix="/funcionario", template_folder='templates')

''' rotas dos formulários '''
@bp_funcionario.route('/funcionario/')
def formListaFuncionario():
    return render_template('formListaFuncionarios.html'), 200

@bp_funcionario.route('/form-funcionario/', methods=['GET'])
def formFuncionario():
    return render_template('formFuncionario.html')