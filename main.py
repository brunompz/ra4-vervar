from datetime import date

from CalcularSaldo.TDD.Saldo import Saldo
from EditarLancamento.TDD.EditarLancamento import EditarLancamento, validarIndice
from ExcluirLancamento.TDD.ExcluirLancamento import ExcluirLancamento
from RegistrarDespesas.TDD.Despesas import Despesas
from RegistrarDespesasRecorrentes.TDD.DespesasRecorrentes import DespesasRecorrentes
from RegistrarReceitas.TDD.Receitas import Receitas
from RegistrarReceitasRecorrentes.TDD.ReceitasRecorrentes import ReceitasRecorrentes


def exibir_menu():
    """Exibe as opções do menu principal e retorna a escolha do usuário."""
    print("\n=== Sistema de Gestão de Gastos Pessoais ===")
    print("1 - Registrar despesa")
    print("2 - Registrar receita")
    print("3 - Registrar despesa recorrente mensal")
    print("4 - Registrar receita recorrente mensal")
    print("5 - Calcular saldo")
    print("6 - Editar lançamento")
    print("7 - Excluir lançamento")
    print("0 - Sair")
    return input("Escolha uma opção: ").strip()


def registrar_lancamento(titulo, servico, mensagem_sucesso, recorrente=False):
    """Solicita os dados no terminal e realiza o registro no módulo correspondente."""
    print(f"\n--- {titulo} ---")
    categoria = input("Categoria: ")
    valor = input("Valor: ")

    try:
        if recorrente:
            dia = input("Dia de ocorrência: ")
            servico.registrar(categoria, valor, dia)
            hoje = date.today()
            servico.itens[-1]["ano_inicio"] = hoje.year
            servico.itens[-1]["mes_inicio"] = hoje.month
        else:
            servico.registrar(categoria, valor)
        print(mensagem_sucesso)
    except ValueError as erro:
        print(erro)


def exibir_saldo(saldo, receitas, despesas, receitas_recorrentes, despesas_recorrentes):
    """Calcula e exibe o saldo atual considerando lançamentos normais e recorrentes acumulados até hoje."""
    print("\n--- Cálculo de Saldo ---")

    try:
        valor_saldo = saldo.calcular(
            receitas.itens,
            despesas.itens,
            receitas_recorrentes.itens,
            despesas_recorrentes.itens,
            data_atual=date.today(),
        )
        valor_formatado = f"{valor_saldo:.2f}".replace(".", ",")
        print(f"Saldo atual: R$ {valor_formatado}")
    except ValueError as erro:
        print("Saldo atual: R$ 0,00")
        print(erro)


def editar_lancamento(editor, despesas, receitas):
    """Solicita o lançamento a ser editado e os novos dados no terminal."""
    print("\n--- Editar Lançamento ---")
    tipo = input("Tipo (1 - Despesa, 2 - Receita): ").strip()
    if tipo not in ("1", "2"):
        print("Opção inválida. Tente novamente.")
        return
    itens = despesas.itens if tipo == "1" else receitas.itens

    try:
        indice = int(input("Número do lançamento: ")) - 1
    except ValueError:
        print("Lançamento não encontrado")
        return

    try:
        validarIndice(itens, indice)
    except ValueError as erro:
        print(erro)
        return

    categoria = input("Nova categoria: ")
    valor = input("Novo valor: ")

    try:
        editor.editar(itens, indice, categoria, valor)
        print("Lançamento editado com sucesso")
    except ValueError as erro:
        print(erro)


def excluir_lancamento(excluidor, despesas, receitas):
    """Solicita o lançamento a ser excluído no terminal."""
    print("\n--- Excluir Lançamento ---")
    tipo = input("Tipo (1 - Despesa, 2 - Receita): ").strip()
    if tipo not in ("1", "2"):
        print("Opção inválida. Tente novamente.")
        return
    itens = despesas.itens if tipo == "1" else receitas.itens

    try:
        indice = int(input("Número do lançamento: ")) - 1
    except ValueError:
        print("Lançamento não encontrado")
        return

    try:
        excluidor.excluir(itens, indice)
        print("Lançamento excluído com sucesso")
    except ValueError as erro:
        print(erro)


def main():
    """Inicializa os módulos de negócio e executa o loop principal da aplicação."""
    despesas = Despesas()
    receitas = Receitas()
    despesas_recorrentes = DespesasRecorrentes()
    receitas_recorrentes = ReceitasRecorrentes()
    saldo = Saldo()
    editor = EditarLancamento()
    excluidor = ExcluirLancamento()

    opcoes = {
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
            exibir_saldo(saldo, receitas, despesas, receitas_recorrentes, despesas_recorrentes)
            continue

        if escolha == "6":
            editar_lancamento(editor, despesas, receitas)
            continue

        if escolha == "7":
            excluir_lancamento(excluidor, despesas, receitas)
            continue

        if escolha not in opcoes:
            print("Opção inválida. Tente novamente.")
            continue

        titulo, servico, mensagem_sucesso, recorrente = opcoes[escolha]
        registrar_lancamento(titulo, servico, mensagem_sucesso, recorrente)


if __name__ == "__main__":
    main()
