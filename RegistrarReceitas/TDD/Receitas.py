class Receitas:
    def __init__(self):
        self.itens= []

    def registrar(self, categoria, valor):
        try:
            valor_num = float(valor)
        except:
            raise ValueError("O valor deve ser numérico")
        self.itens.append({"categoria": categoria, "valor": valor})
    