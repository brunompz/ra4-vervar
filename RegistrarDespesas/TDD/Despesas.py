def validarValor(valor):
    if float(valor) <= 0:
                raise ValueError("O valor deve ser maior que zero")

class Despesas:
    def __init__(self):
        self.itens = []

    def registrar(self, categoria, valor):
        try:
            valor_num = float(valor)
        except:
            raise ValueError("O valor deve ser numérico") 
        validarValor(valor)
        self.itens.append({"categoria": categoria, "valor": valor})