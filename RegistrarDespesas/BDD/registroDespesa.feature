# language: pt
Funcionalidade: Registro de despesas
    Como usuário do sistema de gestão de gastos pessoais
    Quero registrar minhas despesas
    Para acompanhar quanto gasto por categoria

Cenário: Registrar despesa com sucesso
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "1" de registrar despesa
    E seleciona a categoria "Alimentação" na lista de categorias
    E informa o valor "1000"
    Então o sistema deve registrar a despesa com categoria "Alimentação" e valor R$ 1000,00
    E deve exibir a mensagem "Despesa registrada com sucesso"
    E deve retornar ao menu principal

Cenário: Valor não numérico
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "1" de registrar despesa
    E seleciona a categoria "Alimentação" na lista de categorias
    E informa o valor "abc"
    Então o sistema deve exibir a mensagem "O valor deve ser numérico"
    E não deve registrar nenhuma despesa

Cenário: Valor negativo
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "1" de registrar despesa
    E seleciona a categoria "Alimentação" na lista de categorias
    E informa o valor "-50"
    Então o sistema deve exibir a mensagem "O valor deve ser maior que zero"
    E não deve registrar nenhuma despesa

Cenário: Categoria inexistente na seleção
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "1" de registrar despesa
    E informa um número de categoria inexistente
    Então o sistema deve exibir a mensagem "Categoria não encontrada"
    E não deve registrar nenhuma despesa
