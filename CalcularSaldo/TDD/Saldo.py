def somarValores(itens):
    return sum(float(item["valor"]) for item in itens)


def somarRecorrentes(itens, dia_atual=None):
    if dia_atual is None:
        return somarValores(itens)
    filtrados = [item for item in itens if int(item["dia"]) <= int(dia_atual)]
    return somarValores(filtrados)


class Saldo:
    def calcular(self, receitas, despesas, receitas_recorrentes=None, despesas_recorrentes=None, dia_atual=None):
        receitas_recorrentes = receitas_recorrentes or []
        despesas_recorrentes = despesas_recorrentes or []
        if not receitas and not despesas and not receitas_recorrentes and not despesas_recorrentes:
            raise ValueError("Nenhum lançamento registrado")
        total_receitas = somarValores(receitas) + somarRecorrentes(receitas_recorrentes, dia_atual)
        total_despesas = somarValores(despesas) + somarRecorrentes(despesas_recorrentes, dia_atual)
        return total_receitas - total_despesas
