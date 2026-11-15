import pytest
from RegistrarDespesasRecorrentes.TDD.DespesasRecorrentes import DespesasRecorrentes

@pytest.fixture
def despesas_recorrentes():
    return DespesasRecorrentes()

def test_registrarDespesaRecorrenteComSucesso(despesas_recorrentes):
    despesas_recorrentes.registrar("Energia", 250.00, 5)
    assert despesas_recorrentes.itens == [{"categoria": "Energia", "valor": 250.00, "dia": 5}]

def test_registrarDespesaRecorrenteComValorNaoNumerico(despesas_recorrentes):
    with pytest.raises(ValueError, match="Valor inválido"):
        despesas_recorrentes.registrar("Energia", "abc", 5)

def test_registrarDespesaRecorrenteComValorNegativo(despesas_recorrentes):
    with pytest.raises(ValueError, match="O valor deve ser maior que zero"):
        despesas_recorrentes.registrar("Energia", -50, 5)

def test_registrarDespesaRecorrenteComValorVazio(despesas_recorrentes):
    with pytest.raises(ValueError, match="O valor é obrigatório"):
        despesas_recorrentes.registrar("Energia", "", 5)

def test_registrarDespesaRecorrenteComCategoriaVazia(despesas_recorrentes):
    with pytest.raises(ValueError, match="A categoria é obrigatória"):
        despesas_recorrentes.registrar("", 250.00, 5)
