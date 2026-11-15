def validarCategoria(categoria):
    if not categoria.strip():
        raise ValueError("A categoria é obrigatória")


def validarValor(valor):
    try:
        valor_num = float(valor)
    except (ValueError, TypeError):
        raise ValueError("O valor deve ser numérico")
    if valor_num <= 0:
        raise ValueError("O valor deve ser maior que zero")


def validarIndice(itens, indice):
    if indice < 0 or indice >= len(itens):
        raise ValueError("Lançamento não encontrado")


class EditarLancamento:
    def editar(self, itens, indice, categoria, valor):
        validarIndice(itens, indice)
        validarCategoria(categoria)
        validarValor(valor)
        itens[indice]["categoria"] = categoria
        itens[indice]["valor"] = valor
