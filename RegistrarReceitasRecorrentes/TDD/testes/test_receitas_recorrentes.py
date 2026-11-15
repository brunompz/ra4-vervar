import pytest
from RegistrarReceitasRecorrentes.TDD.ReceitasRecorrentes import ReceitasRecorrentes

@pytest.fixture
def receitas_recorrentes():
    return ReceitasRecorrentes()

def test_registrarReceitaRecorrenteComSucesso(receitas_recorrentes):
    receitas_recorrentes.registrar("Salário", 3000.00, 5)
    assert receitas_recorrentes.itens == [{"categoria": "Salário", "valor": 3000.00, "dia": 5}]

def test_registrarReceitaRecorrenteComValorNaoNumerico(receitas_recorrentes):
    with pytest.raises(ValueError, match="Valor inválido"):
        receitas_recorrentes.registrar("Salário", "abc", 5)
