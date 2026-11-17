# language: pt
Funcionalidade: Filtrar lançamentos por categoria
    Como usuário do sistema de gestão de gastos pessoais
    Quero filtrar meus lançamentos por categoria
    Para ver apenas os gastos e ganhos de um tipo específico

Cenário: Filtrar despesas por categoria com sucesso
    Dado que o usuário executou a aplicação no terminal
    E existe a categoria "Alimentação" cadastrada na posição "1"
    E existe uma despesa registrada com categoria "Alimentação" e valor R$ 100,00
    E existe uma despesa registrada com categoria "Transporte" e valor R$ 50,00
    Quando o usuário seleciona a opção "10" de filtrar lançamentos por categoria
    E escolhe o tipo "1" de despesa
    E escolhe a categoria de número "1"
    Então o sistema deve exibir apenas a despesa de categoria "Alimentação" e valor R$ 100,00
    E deve retornar ao menu principal

Cenário: Categoria sem lançamentos
    Dado que o usuário executou a aplicação no terminal
    E existe a categoria "Lazer" cadastrada na posição "4"
    E não existem despesas registradas com a categoria "Lazer"
    Quando o usuário seleciona a opção "10" de filtrar lançamentos por categoria
    E escolhe o tipo "1" de despesa
    E escolhe a categoria de número "4"
    Então o sistema deve exibir a mensagem "Nenhum lançamento encontrado para esta categoria"

Cenário: Nenhuma categoria cadastrada
    Dado que o usuário executou a aplicação no terminal
    E não existem categorias cadastradas
    Quando o usuário seleciona a opção "10" de filtrar lançamentos por categoria
    E escolhe o tipo "1" de despesa
    Então o sistema deve exibir a mensagem "Nenhuma categoria cadastrada. Cadastre uma categoria primeiro"
