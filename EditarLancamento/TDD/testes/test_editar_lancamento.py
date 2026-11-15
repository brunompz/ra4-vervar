import pytest
from EditarLancamento.TDD.EditarLancamento import EditarLancamento

@pytest.fixture
def editor():
    return EditarLancamento()

def test_editarLancamentoComSucesso(editor):
    itens = [{"categoria": "Comida", "valor": 100.00}]
    editor.editar(itens, 0, "Mercado", 150.00)
    assert itens == [{"categoria": "Mercado", "valor": 150.00}]

def test_editarLancamentoInexistente(editor):
    itens = [{"categoria": "Comida", "valor": 100.00}]
    with pytest.raises(ValueError, match="Lançamento não encontrado"):
        editor.editar(itens, 5, "Mercado", 150.00)

def test_editarLancamentoEmListaVazia(editor):
    with pytest.raises(ValueError, match="Lançamento não encontrado"):
        editor.editar([], 0, "Mercado", 150.00)
