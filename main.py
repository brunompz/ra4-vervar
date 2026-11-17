from datetime import date

from CadastrarCategoria.TDD.Categorias import Categorias
from CalcularSaldo.TDD.Saldo import Saldo, somarRecorrentes, somarValores
from DefinirOrcamento.TDD.Orcamento import Orcamento
from EditarLancamento.TDD.EditarLancamento import EditarLancamento, validarIndice
from ExcluirLancamento.TDD.ExcluirLancamento import ExcluirLancamento
from FiltrarPorCategoria.TDD.Filtro import Filtro
from RegistrarDespesas.TDD.Despesas import Despesas
from RegistrarDespesasRecorrentes.TDD.DespesasRecorrentes import DespesasRecorrentes
from RegistrarReceitas.TDD.Receitas import Receitas
from RegistrarReceitasRecorrentes.TDD.ReceitasRecorrentes import ReceitasRecorrentes
from VisualizarTotalPorCategoria.TDD.TotalPorCategoria import TotalPorCategoria

CATEGORIAS_PADRAO = [
    "Alimentação",
    "Transporte",
    "Moradia",
    "Lazer",
    "Saúde",
    "Salário",
    "Outros",
]


def formatar_valor(valor):
    """Formata um valor numérico para o padrão monetário brasileiro."""
    return f"R$ {float(valor):.2f}".replace(".", ",")


def normalizar_valor(valor):
    """Normaliza entrada numérica aceitando vírgula ou ponto decimal."""
    return valor.strip().replace(",", ".")


def formatar_lancamento(item, recorrente=False):
    """Retorna uma representação legível de um lançamento para exibição no terminal."""
    texto = f"{item['categoria']} | {formatar_valor(item['valor'])}"
    if recorrente or "dia" in item:
        texto += f" (dia {item['dia']})"
    return texto


def exibir_menu():
    """Exibe as opções do menu principal e retorna a escolha do usuário."""
    print("\n============================================")
    print("   Sistema de Gestão de Gastos Pessoais")
    print("============================================\n")
    print(" 1 - Registrar despesa")
    print(" 2 - Registrar receita")
    print(" 3 - Registrar despesa recorrente mensal")
    print(" 4 - Registrar receita recorrente mensal")
    print(" 5 - Calcular saldo")
    print(" 6 - Editar lançamento")
    print(" 7 - Excluir lançamento")
    print(" 8 - Definir orçamento do mês")
    print(" 9 - Total por categoria")
    print("10 - Filtrar por categoria")
    print("11 - Cadastrar categoria")
    print(" 0 - Sair\n")
    return input("Escolha uma opção: ").strip()


def selecionar_categoria(categorias):
    """Lista as categorias disponíveis e retorna a selecionada pelo usuário."""
    if not categorias.itens:
        print("\nNenhuma categoria cadastrada. Cadastre uma categoria primeiro")
        return None

    print("\nCategorias disponíveis:")
    for i, nome in enumerate(categorias.itens, start=1):
        print(f" {i} - {nome}")

    try:
        indice = int(input("\nEscolha o número da categoria: ").strip()) - 1
        return categorias.obter(indice)
    except ValueError as erro:
        if "Categoria não encontrada" in str(erro):
            print(f"\n{erro}")
        else:
            print("\nCategoria não encontrada")
        return None


def selecionar_tipo_lancamento(despesas, receitas, despesas_recorrentes, receitas_recorrentes):
    """Solicita o tipo de lançamento e retorna a lista correspondente e se é recorrente."""
    print("\nTipo de lançamento:")
    print(" 1 - Despesa")
    print(" 2 - Receita")
    print(" 3 - Despesa recorrente")
    print(" 4 - Receita recorrente")
    tipo = input("\nEscolha o tipo: ").strip()

    tipos = {
        "1": (despesas.itens, False),
        "2": (receitas.itens, False),
        "3": (despesas_recorrentes.itens, True),
        "4": (receitas_recorrentes.itens, True),
    }
    if tipo not in tipos:
        print("\nOpção inválida. Tente novamente.")
        return None, False
    return tipos[tipo]


def selecionar_lancamento(itens, recorrente=False):
    """Exibe os lançamentos registrados com seus índices e retorna o índice escolhido."""
    if not itens:
        print("\nNenhum lançamento registrado")
        return None

    print("\nLançamentos registrados:")
    for i, item in enumerate(itens, start=1):
        print(f" {i} - {formatar_lancamento(item, recorrente)}")
    print(" 0 - Cancelar")

    escolha = input("\nEscolha o número do lançamento: ").strip()
    if escolha == "0":
        print("\nOperação cancelada.")
        return None

    try:
        indice = int(escolha) - 1
        validarIndice(itens, indice)
        return indice
    except ValueError:
        print("\nLançamento não encontrado")
        return None


def registrar_lancamento(titulo, servico, mensagem_sucesso, categorias, recorrente=False):
    """Solicita os dados no terminal e realiza o registro no módulo correspondente."""
    print(f"\n--- {titulo} ---")
    categoria = selecionar_categoria(categorias)
    if categoria is None:
        return

    valor = normalizar_valor(input("\nValor: "))

    try:
        if recorrente:
            dia = input("Dia de ocorrência: ").strip()
            servico.registrar(categoria, valor, dia)
            hoje = date.today()
            servico.itens[-1]["ano_inicio"] = hoje.year
            servico.itens[-1]["mes_inicio"] = hoje.month
        else:
            servico.registrar(categoria, valor)
        print(f"\n{mensagem_sucesso}")
    except ValueError as erro:
        print(f"\n{erro}")


def exibir_saldo(saldo, receitas, despesas, receitas_recorrentes, despesas_recorrentes, orcamento):
    """Calcula e exibe o saldo atual e alerta se as despesas ultrapassarem o orçamento do mês."""
    print("\n--- Cálculo de Saldo ---\n")
    hoje = date.today()

    try:
        valor_saldo = saldo.calcular(
            receitas.itens,
            despesas.itens,
            receitas_recorrentes.itens,
            despesas_recorrentes.itens,
            data_atual=hoje,
        )
        print(f"Saldo atual: {formatar_valor(valor_saldo)}")

        if orcamento.valor is not None and (orcamento.ano, orcamento.mes) == (hoje.year, hoje.month):
            total_despesas = somarValores(despesas.itens) + somarRecorrentes(
                despesas_recorrentes.itens, data_atual=hoje
            )
            if total_despesas > orcamento.valor:
                print(
                    f"\nATENÇÃO: Suas despesas ({formatar_valor(total_despesas)}) "
                    f"ultrapassaram o orçamento do mês ({formatar_valor(orcamento.valor)})!"
                )
            else:
                restante = orcamento.valor - total_despesas
                print(
                    f"\nOrçamento do mês: {formatar_valor(orcamento.valor)} "
                    f"| Restante: {formatar_valor(restante)}"
                )
    except ValueError as erro:
        print("Saldo atual: R$ 0,00")
        print(f"\n{erro}")


def editar_lancamento(editor, categorias, despesas, receitas, despesas_recorrentes, receitas_recorrentes):
    """Lista os lançamentos, solicita o item a editar e atualiza categoria e valor."""
    print("\n--- Editar Lançamento ---")
    itens, recorrente = selecionar_tipo_lancamento(
        despesas, receitas, despesas_recorrentes, receitas_recorrentes
    )
    if itens is None:
        return

    indice = selecionar_lancamento(itens, recorrente)
    if indice is None:
        return

    print("\nSelecione a nova categoria:")
    categoria = selecionar_categoria(categorias)
    if categoria is None:
        return

    valor = normalizar_valor(input("\nNovo valor: "))

    try:
        editor.editar(itens, indice, categoria, valor)
        print("\nLançamento editado com sucesso")
    except ValueError as erro:
        print(f"\n{erro}")


def excluir_lancamento(excluidor, despesas, receitas, despesas_recorrentes, receitas_recorrentes):
    """Lista os lançamentos e exclui o item escolhido no terminal."""
    print("\n--- Excluir Lançamento ---")
    itens, recorrente = selecionar_tipo_lancamento(
        despesas, receitas, despesas_recorrentes, receitas_recorrentes
    )
    if itens is None:
        return

    indice = selecionar_lancamento(itens, recorrente)
    if indice is None:
        return

    try:
        excluidor.excluir(itens, indice)
        print("\nLançamento excluído com sucesso")
    except ValueError as erro:
        print(f"\n{erro}")


def definir_orcamento(orcamento):
    """Solicita o valor e define o orçamento do mês."""
    print("\n--- Definir Orçamento do Mês ---\n")
    valor = normalizar_valor(input("Valor: "))
    try:
        orcamento.definir(valor)
        print("\nOrçamento definido com sucesso")
    except ValueError as erro:
        print(f"\n{erro}")


def exibir_total_por_categoria(total, despesas, receitas, despesas_recorrentes, receitas_recorrentes):
    """Exibe o total por categoria para despesas ou receitas (normais e recorrentes)."""
    print("\n--- Total por Categoria ---\n")
    print(" 1 - Despesas")
    print(" 2 - Receitas")
    tipo = input("\nEscolha o tipo: ").strip()

    if tipo == "1":
        itens = despesas.itens + despesas_recorrentes.itens
    elif tipo == "2":
        itens = receitas.itens + receitas_recorrentes.itens
    else:
        print("\nOpção inválida. Tente novamente.")
        return

    print()
    try:
        totais = total.calcular(itens)
        for categoria, valor in totais.items():
            print(f"{categoria}: {formatar_valor(valor)}")
    except ValueError as erro:
        print(erro)


def filtrar_por_categoria(filtro, categorias, despesas, receitas, despesas_recorrentes, receitas_recorrentes):
    """Filtra e exibe lançamentos por tipo e categoria selecionados."""
    print("\n--- Filtrar Lançamentos por Categoria ---")
    itens, recorrente = selecionar_tipo_lancamento(
        despesas, receitas, despesas_recorrentes, receitas_recorrentes
    )
    if itens is None:
        return

    categoria = selecionar_categoria(categorias)
    if categoria is None:
        return

    try:
        encontrados = filtro.filtrar(itens, categoria)
        if not encontrados:
            print("\nNenhum lançamento encontrado para esta categoria")
            return

        print(f"\nLançamentos na categoria '{categoria}':\n")
        for i, item in enumerate(encontrados, start=1):
            print(f" {i} - {formatar_lancamento(item, recorrente)}")
    except ValueError as erro:
        print(f"\n{erro}")


def cadastrar_categoria(categorias):
    """Exibe as categorias cadastradas e registra uma nova categoria."""
    print("\n--- Cadastrar Categoria ---\n")
    if categorias.itens:
        print("Categorias atuais:", ", ".join(categorias.itens))
    nome = input("\nNome da nova categoria: ")
    try:
        categorias.cadastrar(nome)
        print("\nCategoria cadastrada com sucesso")
    except ValueError as erro:
        print(f"\n{erro}")


def inicializar_categorias():
    """Inicializa o gerenciador de categorias com opções pré-definidas."""
    categorias = Categorias()
    for nome in CATEGORIAS_PADRAO:
        categorias.cadastrar(nome)
    return categorias


def main():
    """Inicializa os módulos de negócio e executa o loop principal da aplicação."""
    categorias = inicializar_categorias()
    despesas = Despesas()
    receitas = Receitas()
    despesas_recorrentes = DespesasRecorrentes()
    receitas_recorrentes = ReceitasRecorrentes()
    saldo = Saldo()
    editor = EditarLancamento()
    excluidor = ExcluirLancamento()
    orcamento = Orcamento()
    total_categoria = TotalPorCategoria()
    filtro = Filtro()

    opcoes_registro = {
        "1": ("Registrar Despesa", despesas, "Despesa registrada com sucesso", False),
        "2": ("Registrar Receita", receitas, "Receita registrada com sucesso", False),
        "3": ("Registrar Despesa Recorrente Mensal", despesas_recorrentes, "Despesa recorrente registrada com sucesso", True),
        "4": ("Registrar Receita Recorrente Mensal", receitas_recorrentes, "Receita recorrente registrada com sucesso", True),
    }

    while True:
        escolha = exibir_menu()

        if escolha == "0":
            print("Encerrando o sistema.")
            break

        if escolha == "5":
            exibir_saldo(saldo, receitas, despesas, receitas_recorrentes, despesas_recorrentes, orcamento)
            continue

        if escolha == "6":
            editar_lancamento(editor, categorias, despesas, receitas, despesas_recorrentes, receitas_recorrentes)
            continue

        if escolha == "7":
            excluir_lancamento(excluidor, despesas, receitas, despesas_recorrentes, receitas_recorrentes)
            continue

        if escolha == "8":
            definir_orcamento(orcamento)
            continue

        if escolha == "9":
            exibir_total_por_categoria(
                total_categoria, despesas, receitas, despesas_recorrentes, receitas_recorrentes
            )
            continue

        if escolha == "10":
            filtrar_por_categoria(filtro, categorias, despesas, receitas, despesas_recorrentes, receitas_recorrentes)
            continue

        if escolha == "11":
            cadastrar_categoria(categorias)
            continue

        if escolha not in opcoes_registro:
            print("Opção inválida. Tente novamente.")
            continue

        titulo, servico, mensagem_sucesso, recorrente = opcoes_registro[escolha]
        registrar_lancamento(titulo, servico, mensagem_sucesso, categorias, recorrente)


if __name__ == "__main__":
    main()
