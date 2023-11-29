from hashlib import sha3_256

class Funcoes(object):
    
    @staticmethod
    def cifraSenha(senha):
        return sha3_256(senha.encode('utf-8')).hexdigest()
    
def validaCredenciais(usuario, senha):
    # Lógica para validar as credenciais, por exemplo, comparando com dados em um banco de dados
    return True  # Substitua isso com sua lógica real