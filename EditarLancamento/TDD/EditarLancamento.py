class EditarLancamento:
    def editar(self, itens, indice, categoria, valor):
        itens[indice]["categoria"] = categoria
        itens[indice]["valor"] = valor
