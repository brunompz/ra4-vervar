class Saldo:
    def calcular(self, receitas, despesas, receitas_recorrentes=None, despesas_recorrentes=None):
        receitas_recorrentes = receitas_recorrentes or []
        despesas_recorrentes = despesas_recorrentes or []
        total_receitas = sum(item["valor"] for item in receitas) + sum(item["valor"] for item in receitas_recorrentes)
        total_despesas = sum(item["valor"] for item in despesas) + sum(item["valor"] for item in despesas_recorrentes)
        return total_receitas - total_despesas
