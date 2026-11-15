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

def test_registrarReceitaRecorrenteComValorNegativo(receitas_recorrentes):
    with pytest.raises(ValueError, match="O valor deve ser maior que zero"):
        receitas_recorrentes.registrar("Salário", -50, 5)

def test_registrarReceitaRecorrenteComValorVazio(receitas_recorrentes):
    with pytest.raises(ValueError, match="O valor é obrigatório"):
        receitas_recorrentes.registrar("Salário", "", 5)

def test_registrarReceitaRecorrenteComCategoriaVazia(receitas_recorrentes):
    with pytest.raises(ValueError, match="A categoria é obrigatória"):
        receitas_recorrentes.registrar("", 3000.00, 5)

def test_registrarReceitaRecorrenteSemDia(receitas_recorrentes):
    with pytest.raises(ValueError, match="O dia de ocorrência é obrigatório"):
        receitas_recorrentes.registrar("Salário", 3000.00, "")
