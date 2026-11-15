from datetime import date
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

def test_desconsiderarRecorrentesComDiaFuturo(saldo):
    receitas = [{"categoria": "Bônus", "valor": 1000.00}]
    despesas = [{"categoria": "Comida", "valor": 400.00}]
    receitas_recorrentes = [{"categoria": "Salário", "valor": 3000.00, "dia": 20}]
    despesas_recorrentes = [{"categoria": "Energia", "valor": 250.00, "dia": 15}]
    assert saldo.calcular(receitas, despesas, receitas_recorrentes, despesas_recorrentes, dia_atual=5) == 600.00

def test_calcularSaldoSemLancamentos(saldo):
    with pytest.raises(ValueError, match="Nenhum lançamento registrado"):
        saldo.calcular([], [], [], [])

def test_calcularSaldoAcumuladoEntreMeses(saldo):
    receitas = [{"categoria": "Bônus", "valor": 1000.00}]
    despesas = []
    receitas_recorrentes = []
    despesas_recorrentes = [{"categoria": "Energia", "valor": 250.00, "dia": 5, "ano_inicio": 2026, "mes_inicio": 11}]
    assert saldo.calcular(receitas, despesas, receitas_recorrentes, despesas_recorrentes, data_atual=date(2026, 12, 2)) == 750.00
    assert saldo.calcular(receitas, despesas, receitas_recorrentes, despesas_recorrentes, data_atual=date(2026, 12, 5)) == 500.00
