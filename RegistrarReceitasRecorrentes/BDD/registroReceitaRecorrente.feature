# language: pt
Funcionalidade: Registro de receitas recorrentes mensais
    Como usuário do sistema de gestão de gastos pessoais
    Quero registrar minhas receitas recorrentes mensais
    Para que sejam creditadas automaticamente todo mês no dia que eu selecionar

Cenário: Registrar uma receita recorrente mensal com sucesso
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "4" de registrar receita recorrente
    E informa a categoria "Salário"
    E informa o valor "3000"
    E informa o dia "05"
    Então o sistema deve registrar a receita recorrente mensal com categoria "Salário", valor R$ 3000,00 e ocorrência no dia 05
    E deve exibir a mensagem "Receita recorrente registrada com sucesso"
    E deve retornar ao menu principal

Cenário: Valor não numérico
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "4" de registrar receita recorrente
    E informa a categoria "Salário"
    E informa o valor "abc"
    E informa o dia "05"
    Então o sistema deve exibir a mensagem "Valor inválido"
    E não deve registrar nenhuma receita recorrente

Cenário: Valor negativo
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "4" de registrar receita recorrente
    E informa a categoria "Salário"
    E informa o valor "-50"
    E informa o dia "05"
    Então o sistema deve exibir a mensagem "O valor deve ser maior que zero"
    E não deve registrar nenhuma receita recorrente

Cenário: Falta de preenchimento do campo de valor
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "4" de registrar receita recorrente
    E informa a categoria "Salário"
    E informa o valor ""
    E informa o dia "05"
    Então o sistema deve exibir a mensagem "O valor é obrigatório"
    E não deve registrar nenhuma receita recorrente

Cenário: Categoria vazia
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "4" de registrar receita recorrente
    E informa a categoria ""
    E informa o valor "3000"
    E informa o dia "05"
    Então o sistema deve exibir a mensagem "A categoria é obrigatória"
    E não deve registrar nenhuma receita recorrente

Cenário: Falta de seleção do dia específico
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "4" de registrar receita recorrente
    E informa a categoria "Salário"
    E informa o valor "3000"
    E informa o dia ""
    Então o sistema deve exibir a mensagem "O dia de ocorrência é obrigatório"
    E não deve registrar nenhuma receita recorrente
