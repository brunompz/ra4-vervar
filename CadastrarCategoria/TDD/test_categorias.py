import pytest
from CadastrarCategoria.TDD.Categorias import Categorias

@pytest.fixture
def categorias():
    return Categorias()

def test_cadastrarCategoriaComSucesso(categorias):
    categorias.cadastrar("Comida")
    assert categorias.itens == ["Comida"]

def test_cadastrarCategoriaVazia(categorias):
    with pytest.raises(ValueError, match="O nome da categoria é obrigatório"):
        categorias.cadastrar("   ")
    assert categorias.itens == []

def test_cadastrarCategoriaRemoveEspacosNasPontas(categorias):
    categorias.cadastrar("  Comida  ")
    assert categorias.itens == ["Comida"]

def test_cadastrarCategoriaDuplicada(categorias):
    categorias.cadastrar("Comida")
    with pytest.raises(ValueError, match="Categoria já cadastrada"):
        categorias.cadastrar("comida")
    assert categorias.itens == ["Comida"]
def test_obterCategoriaPorIndice(categorias):
    categorias.cadastrar("Comida")
    categorias.cadastrar("Transporte")
    assert categorias.obter(1) == "Transporte"
def test_obterCategoriaInexistente(categorias):
    with pytest.raises(ValueError, match="Categoria não encontrada"):
        categorias.obter(0)

