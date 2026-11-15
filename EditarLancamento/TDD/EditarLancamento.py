class EditarLancamento:
    def editar(self, itens, indice, categoria, valor):
        if indice < 0 or indice >= len(itens):
            raise ValueError("Lançamento não encontrado")
        itens[indice]["categoria"] = categoria
        itens[indice]["valor"] = valor
