import pytest
from VisualizarTotalPorCategoria.TDD.TotalPorCategoria import TotalPorCategoria

@pytest.fixture
def total():
    return TotalPorCategoria()

def test_totalDeUmaCategoria(total):
    itens = [{"categoria": "Comida", "valor": 300.00}]
    assert total.calcular(itens) == {"Comida": 300.00}

def test_somarMesmaCategoria(total):
    itens = [{"categoria": "Comida", "valor": 300.00},
             {"categoria": "Comida", "valor": 200.00}]
    assert total.calcular(itens) == {"Comida": 500.00}

def test_totalDeVariasCategorias(total):
    itens = [{"categoria": "Comida", "valor": 300.00},
             {"categoria": "Transporte", "valor": 100.00}]
    assert total.calcular(itens) == {"Comida": 300.00, "Transporte": 100.00}

def test_valoresEmTexto(total):
    itens = [{"categoria": "Comida", "valor": "300"},
             {"categoria": "Comida", "valor": "50.5"}]
    assert total.calcular(itens) == {"Comida": 350.50}

def test_semLancamentos(total):
    with pytest.raises(ValueError, match="Nenhum lançamento registrado"):
        total.calcular([])
