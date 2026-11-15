def validarValor(valor):
    if valor is None or (isinstance(valor, str) and not valor.strip()):
        raise ValueError("O valor é obrigatório")
    try:
        valor_num = float(valor)
    except (ValueError, TypeError):
        raise ValueError("Valor inválido")
    if valor_num <= 0:
        raise ValueError("O valor deve ser maior que zero")


def validarCategoria(categoria):
    if not categoria or not categoria.strip():
        raise ValueError("A categoria é obrigatória")


def validarDia(dia):
    if dia is None or (isinstance(dia, str) and not dia.strip()):
        raise ValueError("O dia de ocorrência é obrigatório")


class DespesasRecorrentes:
    def __init__(self):
        self.itens = []

    def registrar(self, categoria, valor, dia):
        validarCategoria(categoria)
        validarValor(valor)
        validarDia(dia)
        self.itens.append({"categoria": categoria, "valor": valor, "dia": dia})
