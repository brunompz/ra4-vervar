import pytest
from RegistrarReceitas.TDD.Receitas import Receitas

@pytest.fixture
def receitas():
    return Receitas()

def test_registrarReceitaComSucesso(receitas):
    receitas.registrar("Salário", 3000)
    assert receitas.itens == [{"categoria": "Salário", "valor": 3000}]


def test_registrarReceitaComValorNaoNumerico(receitas):
    with pytest.raises(ValueError, match="O valor deve ser numérico"):
        receitas.registrar("Salário", "abc")
