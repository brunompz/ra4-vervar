from RegistrarDespesasRecorrentes.TDD.DespesasRecorrentes import validarValor


class ReceitasRecorrentes:
    def __init__(self):
        self.itens = []

    def registrar(self, categoria, valor, dia):
        validarValor(valor)
        self.itens.append({"categoria": categoria, "valor": valor, "dia": dia})
