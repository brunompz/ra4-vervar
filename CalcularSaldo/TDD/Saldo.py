def somarValores(itens):
    return sum(float(item["valor"]) for item in itens)


def calcularOcorrencias(item, data_atual):
    ano_inicio = item.get("ano_inicio", data_atual.year)
    mes_inicio = item.get("mes_inicio", data_atual.month)
    meses = (data_atual.year - ano_inicio) * 12 + (data_atual.month - mes_inicio)
    ocorrencias = meses + 1 if data_atual.day >= int(item["dia"]) else meses
    return max(0, ocorrencias)


def somarRecorrentes(itens, dia_atual=None, data_atual=None):
    if data_atual is not None:
        return sum(float(item["valor"]) * calcularOcorrencias(item, data_atual) for item in itens)
    if dia_atual is None:
        return somarValores(itens)
    filtrados = [item for item in itens if int(item["dia"]) <= int(dia_atual)]
    return somarValores(filtrados)


def validarLancamentos(receitas, despesas, receitas_recorrentes, despesas_recorrentes):
    if not receitas and not despesas and not receitas_recorrentes and not despesas_recorrentes:
        raise ValueError("Nenhum lançamento registrado")


class Saldo:
    def calcular(self, receitas, despesas, receitas_recorrentes=None, despesas_recorrentes=None, dia_atual=None, data_atual=None):
        receitas_recorrentes = receitas_recorrentes or []
        despesas_recorrentes = despesas_recorrentes or []
        validarLancamentos(receitas, despesas, receitas_recorrentes, despesas_recorrentes)
        total_receitas = somarValores(receitas) + somarRecorrentes(receitas_recorrentes, dia_atual, data_atual)
        total_despesas = somarValores(despesas) + somarRecorrentes(despesas_recorrentes, dia_atual, data_atual)
        return total_receitas - total_despesas
