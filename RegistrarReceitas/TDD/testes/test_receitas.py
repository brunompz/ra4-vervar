import pytest
from RegistrarReceitas.TDD.Receitas import Receitas

@pytest.fixture
def receitas():
    return Receitas()

def test_registrarReceitaComSucesso():
    receitas.registrar("Salário", 3000)
    assert receitas.item("categoria": "Salário", "valor": 3000)