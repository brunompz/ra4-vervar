import pytest
from FiltrarPorCategoria.TDD.Filtro import Filtro

@pytest.fixture
def filtro():
    return Filtro()

@pytest.fixture
def itens():
    return [
        {"categoria": "Comida", "valor": 100.00},
        {"categoria": "Transporte", "valor": 50.00},
        {"categoria": "Comida", "valor": 30.00},
    ]

def test_filtrarPorCategoriaComSucesso(filtro, itens):
    assert filtro.filtrar(itens, "Comida") == [
        {"categoria": "Comida", "valor": 100.00},
        {"categoria": "Comida", "valor": 30.00},
    ]
def test_filtrarIgnoraMaiusculas(filtro, itens):
    assert len(filtro.filtrar(itens, "comida")) == 2

def test_filtrarCategoriaSemLancamentos(filtro, itens):
    assert filtro.filtrar(itens, "Lazer") == []

def test_filtrarEmListaVazia(filtro):
    assert filtro.filtrar([], "Comida") == []
def test_filtrarComCategoriaVazia(filtro, itens):
    with pytest.raises(ValueError, match="A categoria é obrigatória"):
        filtro.filtrar(itens, "")
def test_filtrarNaoAlteraListaOriginal(filtro, itens):
    filtro.filtrar(itens, "Comida")
    assert len(itens) == 3