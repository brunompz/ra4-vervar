from RegistrarDespesas.TDD.Despesas import Despesas
from RegistrarReceitas.TDD.Receitas import Receitas
from RegistrarDespesasRecorrentes.TDD.DespesasRecorrentes import DespesasRecorrentes
from RegistrarReceitasRecorrentes.TDD.ReceitasRecorrentes import ReceitasRecorrentes


def exibir_menu():
    """Exibe as opções do menu principal e retorna a escolha do usuário."""
    print("\n=== Sistema de Gestão de Gastos Pessoais ===")
    print("1 - Registrar despesa")
    print("2 - Registrar receita")
    print("3 - Registrar despesa recorrente mensal")
    print("4 - Registrar receita recorrente mensal")
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
        else:
            servico.registrar(categoria, valor)
        print(mensagem_sucesso)
    except ValueError as erro:
        print(erro)


def main():
    """Inicializa os módulos de negócio e executa o loop principal da aplicação."""
    despesas = Despesas()
    receitas = Receitas()
    despesas_recorrentes = DespesasRecorrentes()
    receitas_recorrentes = ReceitasRecorrentes()

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

        if escolha not in opcoes:
            print("Opção inválida. Tente novamente.")
            continue

        titulo, servico, mensagem_sucesso, recorrente = opcoes[escolha]
        registrar_lancamento(titulo, servico, mensagem_sucesso, recorrente)


if __name__ == "__main__":
    main()
