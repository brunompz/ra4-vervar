# language: pt
Funcionalidade: Visualizar total por categoria
    Como usuário do sistema de gestão de gastos pessoais
    Quero visualizar o total de despesas ou receitas em cada categoria
    Para saber onde estou gastando ou ganhando mais

Cenário: Exibir total de uma categoria
    Dado que o usuário executou a aplicação no terminal
    E existe uma despesa "Alimentação" de R$ 300,00
    Quando o usuário seleciona a opção "9" de total por categoria
    E escolhe o tipo "1" de despesas
    Então o sistema deve exibir "Alimentação: R$ 300,00"
    E deve retornar ao menu principal

Cenário: Somar despesas da mesma categoria
    Dado que o usuário executou a aplicação no terminal
    E existe uma despesa "Alimentação" de R$ 300,00
    E existe uma despesa "Alimentação" de R$ 200,00
    Quando o usuário seleciona a opção "9" de total por categoria
    E escolhe o tipo "1" de despesas
    Então o sistema deve exibir "Alimentação: R$ 500,00"

Cenário: Exibir totais de várias categorias
    Dado que o usuário executou a aplicação no terminal
    E existe uma despesa "Alimentação" de R$ 300,00
    E existe uma despesa "Transporte" de R$ 100,00
    Quando o usuário seleciona a opção "9" de total por categoria
    E escolhe o tipo "1" de despesas
    Então o sistema deve exibir "Alimentação: R$ 300,00"
    E deve exibir "Transporte: R$ 100,00"

Cenário: Exibir total de receitas recorrentes por categoria
    Dado que o usuário executou a aplicação no terminal
    E existe uma receita recorrente "Salário" de R$ 3000,00
    Quando o usuário seleciona a opção "9" de total por categoria
    E escolhe o tipo "2" de receitas
    Então o sistema deve exibir "Salário: R$ 3000,00"

Cenário: Sem lançamentos registrados
    Dado que o usuário executou a aplicação no terminal
    E não existem despesas registradas
    Quando o usuário seleciona a opção "9" de total por categoria
    E escolhe o tipo "1" de despesas
    Então o sistema deve exibir a mensagem "Nenhum lançamento registrado"
    E deve retornar ao menu principal
