from datetime import date
import pytest
from DefinirOrcamento.TDD.Orcamento import Orcamento

@pytest.fixture
def orcamento():
    return Orcamento()

def test_definirOrcamentoComSucesso(orcamento):
    orcamento.definir(2000.00)
    assert orcamento.valor == 2000.00

def test_definirOrcamentoGuardaMesEAno(orcamento):
    orcamento.definir(2000.00, data_atual=date(2026, 11, 10))
    assert (orcamento.ano, orcamento.mes) == (2026, 11)

def test_redefinirOrcamentoSubstituiValor(orcamento):
    orcamento.definir(2000.00)
    orcamento.definir(3000.00)
    assert orcamento.valor == 3000.00

def test_definirOrcamentoComValorNaoNumerico(orcamento):
    with pytest.raises(ValueError, match="Valor inválido"):
        orcamento.definir("abc")

def test_definirOrcamentoComValorNegativo(orcamento):
    with pytest.raises(ValueError, match="O valor deve ser maior que zero"):
        orcamento.definir(-100)

def test_definirOrcamentoComValorZero(orcamento):
    with pytest.raises(ValueError, match="O valor deve ser maior que zero"):
        orcamento.definir(0)

def test_definirOrcamentoComValorVazio(orcamento):
    with pytest.raises(ValueError, match="O valor é obrigatório"):
        orcamento.definir("")

def test_orcamentoInvalidoNaoAlteraValorAnterior(orcamento):
    orcamento.definir(2000.00)
    with pytest.raises(ValueError):
        orcamento.definir("abc")
    assert orcamento.valor == 2000.00

