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
        if valor is None or (isinstance(valor, str) and not valor.strip()):
            raise ValueError("O valor é obrigatório")
        validarValor(valor)
        self.itens.append({"categoria": categoria, "valor": valor, "dia": dia})
