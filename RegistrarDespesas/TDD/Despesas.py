def validarValor(valor):
    try:
        valor_num = float(valor)
    except:
        raise ValueError("O valor deve ser numérico") 
    if valor_num <= 0:
        raise ValueError("O valor deve ser maior que zero")
    

class Despesas:
    def __init__(self):
        self.itens = []

    def registrar(self, categoria, valor):
        validarValor(valor)
        self.itens.append({"categoria": categoria, "valor": valor})