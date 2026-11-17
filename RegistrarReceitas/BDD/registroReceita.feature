# language: pt
Funcionalidade: Registro de receitas
    Como usuário do sistema de gestão de gastos pessoais
    Quero registrar minhas receitas
    Para saber quanto dinheiro entrou

Cenário: Registrar receita com sucesso
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "2" de registrar receita
    E seleciona a categoria "Salário" na lista de categorias
    E informa o valor "3000"
    Então o sistema deve registrar a receita com categoria "Salário" e valor R$ 3000,00
    E deve exibir a mensagem "Receita registrada com sucesso"
    E deve retornar ao menu principal

Cenário: Valor não numérico
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "2" de registrar receita
    E seleciona a categoria "Salário" na lista de categorias
    E informa o valor "abc"
    Então o sistema deve exibir a mensagem "O valor deve ser numérico"
    E não deve registrar nenhuma receita

Cenário: Valor negativo
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "2" de registrar receita
    E seleciona a categoria "Salário" na lista de categorias
    E informa o valor "-50"
    Então o sistema deve exibir a mensagem "O valor deve ser positivo"
    E não deve registrar nenhuma receita

Cenário: Categoria inexistente na seleção
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "2" de registrar receita
    E informa um número de categoria inexistente
    Então o sistema deve exibir a mensagem "Categoria não encontrada"
    E não deve registrar nenhuma receita
