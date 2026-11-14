class Despesas:
    def __init__(self):
        self.itens = []

    def registrar(self, categoria, valor):
        self.itens.append({"categoria": categoria, "valor": valor})
        