class Despesas:
    def __init__(self):
        self.itens = []

    def registrar(self, categoria, valor):
        if float(valor) <= 0:
            raise ValueError("O valor deve ser maior que zero")
        self.itens.append({"categoria": categoria, "valor": valor})
