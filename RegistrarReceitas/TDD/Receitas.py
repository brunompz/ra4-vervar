def validarValor(valor):
    try:
        valor_num = float(valor)
    except:
        raise ValueError("O valor deve ser numérico")

class Receitas:
    def __init__(self):
        self.itens= []

    def registrar(self, categoria, valor):
        validarValor(valor)
        if valor <= 0:
            raise ValueError("O valor deve ser positivo")
        self.itens.append({"categoria": categoria, "valor": valor})
    