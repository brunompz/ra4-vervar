def validarNome(nome):
    if nome is None or not str(nome).strip():
        raise ValueError("O nome da categoria é obrigatório")


class Categorias:
    def __init__(self):
        self.itens = []

    def cadastrar(self, nome):
        validarNome(nome)
        nome = nome.strip()
        if any(existente.lower() == nome.lower() for existente in self.itens):
            raise ValueError("Categoria já cadastrada")
        self.itens.append(nome)
    def obter(self, indice):
        if indice < 0 or indice >= len(self.itens):
            raise ValueError("Categoria não encontrada")
        return self.itens[indice]