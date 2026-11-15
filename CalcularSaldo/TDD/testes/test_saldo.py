import pytest
from CalcularSaldo.TDD.Saldo import Saldo

@pytest.fixture
def saldo():
    return Saldo()

def test_calcularSaldoPositivo(saldo):
    receitas = [{"categoria": "Salário", "valor": 3000.00}]
    despesas = [{"categoria": "Comida", "valor": 1000.00}]
    assert saldo.calcular(receitas, despesas) == 2000.00

def test_calcularSaldoNegativo(saldo):
    receitas = [{"categoria": "Salário", "valor": 1000.00}]
    despesas = [{"categoria": "Comida", "valor": 1500.00}]
    assert saldo.calcular(receitas, despesas) == -500.00

def test_calcularSaldoZerado(saldo):
    receitas = [{"categoria": "Salário", "valor": 1000.00}]
    despesas = [{"categoria": "Comida", "valor": 1000.00}]
    assert saldo.calcular(receitas, despesas) == 0.00

def test_calcularSaldoComRecorrentes(saldo):
    receitas = [{"categoria": "Bônus", "valor": 1000.00}]
    despesas = [{"categoria": "Comida", "valor": 500.00}]
    receitas_recorrentes = [{"categoria": "Salário", "valor": 3000.00, "dia": 5}]
    despesas_recorrentes = [{"categoria": "Energia", "valor": 250.00, "dia": 10}]
    assert saldo.calcular(receitas, despesas, receitas_recorrentes, despesas_recorrentes) == 3250.00
