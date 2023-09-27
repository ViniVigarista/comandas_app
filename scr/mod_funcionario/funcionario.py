from flask import Blueprint, render_template
bp_funcionario = Blueprint('funcionario', __name__, url_prefix="/funcionario", template_folder='templates')

''' rotas dos formulários '''
@bp_funcionario.route('/funcionario/')
def formListaFuncionario():
    return render_template('formListaFuncionario.html'), 200