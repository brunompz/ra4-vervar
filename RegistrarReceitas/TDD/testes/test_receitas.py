import pytest
from RegistrarReceitas.TDD.Receitas import Receitas

@pytest.fixture
def receitas():
    return Receitas()

def test_registrarReceitaComSucesso(receitas):
    receitas.registrar("Salário", 3000)
    assert receitas.itens == [{"categoria": "Salário", "valor": 3000}]
