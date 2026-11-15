class DespesasRecorrentes:
    def __init__(self):
        self.itens = []

    def registrar(self, categoria, valor, dia):
        self.itens.append({"categoria": categoria, "valor": valor, "dia": dia})
