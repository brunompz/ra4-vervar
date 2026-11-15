def validarValor(valor):
    try:
        valor_num = float(valor)
    except (ValueError, TypeError):
        raise ValueError("Valor inválido")
    if valor_num <= 0:
        raise ValueError("O valor deve ser maior que zero")


class DespesasRecorrentes:
    def __init__(self):
        self.itens = []

    def registrar(self, categoria, valor, dia):
        validarValor(valor)
        self.itens.append({"categoria": categoria, "valor": valor, "dia": dia})
