import pytest
from RegistrarDespesas.TDD.Despesas import Despesas

@pytest.fixture
def despesas():
    return Despesas()

def test_registrarDespesasComSucesso(despesas):
    despesas.registrar("Comida", 1000.00)
    assert despesas.itens == [{"categoria": "Comida", "valor": 1000.00}]

def test_registrarDespesaComValorNegativo(despesas):
    with pytest.raises(ValueError, match="maior que zero"):
        despesas.registrar("Comida", -50)
    