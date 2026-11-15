# language: pt
Funcionalidade: Registro de receitas recorrentes
    Como usuário do sistema de gestão de gastos pessoais
    Quero registrar minhas receitas recorrentes
    Para que sejam creditadas automaticamente no período de tempo que eu selecionar

Cenário: Registrar uma receita recorrente com sucesso
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "4" de registrar receita recorrente
    E informa a descrição "Salário"
    E informa o valor "3000"
    E informa a recorrência "mensal"
    E informa o dia "05"
    Então o sistema deve registrar a receita recorrente com descrição "Salário", valor R$ 3000,00, recorrência "mensal" e ocorrência no dia 05
    E deve exibir a mensagem "Receita recorrente registrada com sucesso"
    E deve retornar ao menu principal

Cenário: Valor não numérico
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "4" de registrar receita recorrente
    E informa a descrição "Salário"
    E informa o valor "abc"
    E informa a recorrência "mensal"
    E informa o dia "05"
    Então o sistema deve exibir a mensagem "Valor inválido"
    E não deve registrar nenhuma receita recorrente

Cenário: Valor negativo
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "4" de registrar receita recorrente
    E informa a descrição "Salário"
    E informa o valor "-50"
    E informa a recorrência "mensal"
    E informa o dia "05"
    Então o sistema deve exibir a mensagem "O valor deve ser maior que zero"
    E não deve registrar nenhuma receita recorrente

Cenário: Falta de preenchimento do campo de valor
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "4" de registrar receita recorrente
    E informa a descrição "Salário"
    E informa o valor ""
    E informa a recorrência "mensal"
    E informa o dia "05"
    Então o sistema deve exibir a mensagem "O valor é obrigatório"
    E não deve registrar nenhuma receita recorrente

Cenário: Descrição vazia
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "4" de registrar receita recorrente
    E informa a descrição ""
    E informa o valor "3000"
    E informa a recorrência "mensal"
    E informa o dia "05"
    Então o sistema deve exibir a mensagem "A descrição é obrigatória"
    E não deve registrar nenhuma receita recorrente

Cenário: Falta de seleção no campo recorrência
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "4" de registrar receita recorrente
    E informa a descrição "Salário"
    E informa o valor "3000"
    E informa a recorrência ""
    E informa o dia "05"
    Então o sistema deve exibir a mensagem "A recorrência é obrigatória"
    E não deve registrar nenhuma receita recorrente

Cenário: Falta de seleção do dia específico
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "4" de registrar receita recorrente
    E informa a descrição "Salário"
    E informa o valor "3000"
    E informa a recorrência "mensal"
    E informa o dia ""
    Então o sistema deve exibir a mensagem "O dia de ocorrência é obrigatório"
    E não deve registrar nenhuma receita recorrente
