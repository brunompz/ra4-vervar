from RegistrarDespesasRecorrentes.TDD.DespesasRecorrentes import validarValor


class ReceitasRecorrentes:
    def __init__(self):
        self.itens = []

    def registrar(self, categoria, valor, dia):
        if not categoria or not categoria.strip():
            raise ValueError("A categoria é obrigatória")
        validarValor(valor)
        self.itens.append({"categoria": categoria, "valor": valor, "dia": dia})
