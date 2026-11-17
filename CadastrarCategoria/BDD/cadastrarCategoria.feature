# language: pt
Funcionalidade: Cadastrar categoria
    Como usuário do sistema de gestão de gastos pessoais
    Quero cadastrar categorias além das pré-definidas
    Para escolhê-las ao registrar ou editar meus lançamentos

Cenário: Cadastrar categoria com sucesso
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "11" de cadastrar categoria
    E informa o nome "Educação"
    Então o sistema deve cadastrar a categoria "Educação"
    E deve exibir a mensagem "Categoria cadastrada com sucesso"
    E deve retornar ao menu principal

Cenário: Nome vazio
    Dado que o usuário executou a aplicação no terminal
    Quando o usuário seleciona a opção "11" de cadastrar categoria
    E informa o nome ""
    Então o sistema deve exibir a mensagem "O nome da categoria é obrigatório"
    E não deve cadastrar nenhuma categoria

Cenário: Categoria duplicada
    Dado que o usuário executou a aplicação no terminal
    E existe a categoria "Alimentação" cadastrada
    Quando o usuário seleciona a opção "11" de cadastrar categoria
    E informa o nome "alimentação"
    Então o sistema deve exibir a mensagem "Categoria já cadastrada"
    E não deve cadastrar uma nova categoria

Cenário: Registrar lançamento usando categoria cadastrada
    Dado que o usuário executou a aplicação no terminal
    E existem categorias pré-definidas cadastradas
    Quando o usuário seleciona a opção "1" de registrar despesa
    Então o sistema deve listar as categorias cadastradas
    E o usuário escolhe a categoria de número "1"
    E informa o valor "100"
    Então o sistema deve registrar a despesa com a categoria escolhida e valor R$ 100,00

Cenário: Registrar lançamento sem nenhuma categoria cadastrada
    Dado que o usuário executou a aplicação no terminal
    E não existem categorias cadastradas
    Quando o usuário seleciona a opção "1" de registrar despesa
    Então o sistema deve exibir a mensagem "Nenhuma categoria cadastrada. Cadastre uma categoria primeiro"
    E deve retornar ao menu principal
