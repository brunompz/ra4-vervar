from RegistrarDespesasRecorrentes.TDD.DespesasRecorrentes import validarCategoria, validarDia, validarValor


class ReceitasRecorrentes:
    def __init__(self):
        self.itens = []

    def registrar(self, categoria, valor, dia):
        validarCategoria(categoria)
        validarValor(valor)
        validarDia(dia)
        self.itens.append({"categoria": categoria, "valor": valor, "dia": dia})
