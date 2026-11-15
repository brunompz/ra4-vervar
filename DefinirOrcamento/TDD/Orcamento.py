from datetime import date

def validarValor(valor):
    if valor is None or (isinstance(valor, str) and not valor.strip()):
        raise ValueError("O valor é obrigatório")
    try:
        valor_num = float(valor)
    except (ValueError, TypeError):
        raise ValueError("Valor inválido")
    if valor_num <= 0:
        raise ValueError("O valor deve ser maior que zero")

class Orcamento:
    def __init__(self):
        self.valor = None
        self.ano = None
        self.mes = None

    def definir(self, valor, data_atual=None):
        validarValor(valor)
        data_atual = data_atual or date.today()
        self.valor = float(valor)
        self.ano = data_atual.year
        self.mes = data_atual.month
