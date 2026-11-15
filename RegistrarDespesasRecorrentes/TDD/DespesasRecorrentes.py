class DespesasRecorrentes:
    def __init__(self):
        self.itens = []

    def registrar(self, categoria, valor, dia):
        try:
            float(valor)
        except (ValueError, TypeError):
            raise ValueError("Valor inválido")
        self.itens.append({"categoria": categoria, "valor": valor, "dia": dia})
