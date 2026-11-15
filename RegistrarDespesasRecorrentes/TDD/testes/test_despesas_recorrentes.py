import pytest
from RegistrarDespesasRecorrentes.TDD.DespesasRecorrentes import DespesasRecorrentes

@pytest.fixture
def despesas_recorrentes():
    return DespesasRecorrentes()

def test_registrarDespesaRecorrenteComSucesso(despesas_recorrentes):
    despesas_recorrentes.registrar("Energia", 250.00, 5)
    assert despesas_recorrentes.itens == [{"categoria": "Energia", "valor": 250.00, "dia": 5}]
