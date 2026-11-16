def validarCategoria(categoria):
    if categoria is None or not str(categoria).strip():
        raise ValueError("A categoria é obrigatória")


class Filtro:
    def filtrar(self, itens, categoria):
        validarCategoria(categoria)
        alvo = categoria.strip().lower()
        return [item for item in itens if item["categoria"].lower() == alvo]