from RegistrarDespesasRecorrentes.TDD.DespesasRecorrentes import validarCategoria, validarValor


class ReceitasRecorrentes:
    def __init__(self):
        self.itens = []

    def registrar(self, categoria, valor, dia):
        validarCategoria(categoria)
        validarValor(valor)
        if dia is None or (isinstance(dia, str) and not dia.strip()):
            raise ValueError("O dia de ocorrência é obrigatório")
        self.itens.append({"categoria": categoria, "valor": valor, "dia": dia})
