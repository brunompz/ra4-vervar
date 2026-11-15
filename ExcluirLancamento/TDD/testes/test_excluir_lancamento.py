import pytest
from ExcluirLancamento.TDD.ExcluirLancamento import ExcluirLancamento

@pytest.fixture
def excluidor():
    return ExcluirLancamento()

def test_excluirLancamentoComSucesso(excluidor):
    itens = [{"categoria": "Comida", "valor": 100.00}]
    excluidor.excluir(itens, 0)
    assert itens == []

def test_excluirLancamentoNaoAfetaOsDemais(excluidor):
    itens = [{"categoria": "Comida", "valor": 100.00}, {"categoria": "Lazer", "valor": 50.00}]
    excluidor.excluir(itens, 0)
    assert itens == [{"categoria": "Lazer", "valor": 50.00}]

def test_excluirLancamentoInexistente(excluidor):
    itens = [{"categoria": "Comida", "valor": 100.00}]
    with pytest.raises(ValueError, match="Lançamento não encontrado"):
        excluidor.excluir(itens, 5)
    assert itens == [{"categoria": "Comida", "valor": 100.00}]

def test_excluirLancamentoEmListaVazia(excluidor):
    with pytest.raises(ValueError, match="Lançamento não encontrado"):
        excluidor.excluir([], 0)
