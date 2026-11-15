def somarValores(itens):
    return sum(float(item["valor"]) for item in itens)


class Saldo:
    def calcular(self, receitas, despesas, receitas_recorrentes=None, despesas_recorrentes=None, dia_atual=None):
        receitas_recorrentes = receitas_recorrentes or []
        despesas_recorrentes = despesas_recorrentes or []

        if dia_atual is not None:
            receitas_recorrentes = [item for item in receitas_recorrentes if int(item["dia"]) <= int(dia_atual)]
            despesas_recorrentes = [item for item in despesas_recorrentes if int(item["dia"]) <= int(dia_atual)]

        total_receitas = somarValores(receitas) + somarValores(receitas_recorrentes)
        total_despesas = somarValores(despesas) + somarValores(despesas_recorrentes)
        return total_receitas - total_despesas
