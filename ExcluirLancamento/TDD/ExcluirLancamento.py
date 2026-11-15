def validarIndice(itens, indice):
    if indice < 0 or indice >= len(itens):
        raise ValueError("Lançamento não encontrado")


class ExcluirLancamento:
    def excluir(self, itens, indice):
        validarIndice(itens, indice)
        itens.pop(indice)
