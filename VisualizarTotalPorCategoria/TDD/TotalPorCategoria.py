def validarItens(itens):
    if not itens:
        raise ValueError("Nenhum lançamento registrado")


class TotalPorCategoria:
    def calcular(self, itens):
        validarItens(itens)
        totais = {}
        for item in itens:
            categoria = item["categoria"]
            totais[categoria] = totais.get(categoria, 0) + float(item["valor"])
        return totais
