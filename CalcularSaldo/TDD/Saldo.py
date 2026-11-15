class Saldo:
    def calcular(self, receitas, despesas):
        total_receitas = sum(item["valor"] for item in receitas)
        total_despesas = sum(item["valor"] for item in despesas)
        return total_receitas - total_despesas
