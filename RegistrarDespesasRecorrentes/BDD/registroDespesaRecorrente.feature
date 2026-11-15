# language: pt
Funcionalidade: Registro de despesas recorrentes mensais
    Como usuário do sistema de gestão de gastos pessoais
    Quero registrar minhas despesas recorrentes mensais
    Para que sejam debitadas automaticamente todo mês no dia que eu selecionar

Cenário: Registrar uma despesa recorrente mensal com sucesso
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "3" de registrar despesa recorrente
    E informa a categoria "Energia"
    E informa o valor "250"
    E informa o dia "05"
    Então o sistema deve registrar a despesa recorrente mensal com categoria "Energia", valor R$ 250,00 e ocorrência no dia 05
    E deve exibir a mensagem "Despesa recorrente registrada com sucesso"
    E deve retornar ao menu principal

Cenário: Valor não numérico
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "3" de registrar despesa recorrente
    E informa a categoria "Energia"
    E informa o valor "abc"
    E informa o dia "05"
    Então o sistema deve exibir a mensagem "Valor inválido"
    E não deve registrar nenhuma despesa recorrente

Cenário: Valor negativo
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "3" de registrar despesa recorrente
    E informa a categoria "Energia"
    E informa o valor "-50"
    E informa o dia "05"
    Então o sistema deve exibir a mensagem "O valor deve ser maior que zero"
    E não deve registrar nenhuma despesa recorrente

Cenário: Falta de preenchimento do campo de valor
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "3" de registrar despesa recorrente
    E informa a categoria "Energia"
    E informa o valor ""
    E informa o dia "05"
    Então o sistema deve exibir a mensagem "O valor é obrigatório"
    E não deve registrar nenhuma despesa recorrente

Cenário: Categoria vazia
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "3" de registrar despesa recorrente
    E informa a categoria ""
    E informa o valor "250"
    E informa o dia "05"
    Então o sistema deve exibir a mensagem "A categoria é obrigatória"
    E não deve registrar nenhuma despesa recorrente

Cenário: Falta de seleção do dia específico
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "3" de registrar despesa recorrente
    E informa a categoria "Energia"
    E informa o valor "250"
    E informa o dia ""
    Então o sistema deve exibir a mensagem "O dia de ocorrência é obrigatório"
    E não deve registrar nenhuma despesa recorrente
