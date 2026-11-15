# language: pt
Funcionalidade: Editar lançamento
    Como usuário do sistema de gestão de gastos pessoais
    Quero editar um lançamento já registrado
    Para corrigir a categoria ou o valor informado por engano

Cenário: Editar lançamento com sucesso
    Dado que o usuário executou a aplicação no terminal
    E existe uma despesa registrada com categoria "Comida" e valor R$ 100,00
    Quando o usuário seleciona a opção "6" de editar lançamento
    E escolhe o tipo "1" de despesa
    E escolhe o lançamento de número "1"
    E informa a nova categoria "Mercado"
    E informa o novo valor "150"
    Então o sistema deve atualizar o lançamento para categoria "Mercado" e valor R$ 150,00
    E deve exibir a mensagem "Lançamento editado com sucesso"
    E deve retornar ao menu principal

Cenário: Editar lançamento inexistente
    Dado que o usuário executou a aplicação no terminal
    E não existem despesas registradas
    Quando o usuário seleciona a opção "6" de editar lançamento
    E escolhe o tipo "1" de despesa
    E escolhe o lançamento de número "1"
    Então o sistema deve exibir a mensagem "Lançamento não encontrado"
    E deve retornar ao menu principal

Cenário: Editar lançamento com valor inválido
    Dado que o usuário executou a aplicação no terminal
    E existe uma despesa registrada com categoria "Comida" e valor R$ 100,00
    Quando o usuário seleciona a opção "6" de editar lançamento
    E escolhe o tipo "1" de despesa
    E escolhe o lançamento de número "1"
    E informa a nova categoria "Mercado"
    E informa o novo valor "-50"
    Então o sistema deve exibir a mensagem "O valor deve ser maior que zero"
    E o lançamento deve permanecer com categoria "Comida" e valor R$ 100,00

Cenário: Editar lançamento com categoria vazia
    Dado que o usuário executou a aplicação no terminal
    E existe uma despesa registrada com categoria "Comida" e valor R$ 100,00
    Quando o usuário seleciona a opção "6" de editar lançamento
    E escolhe o tipo "1" de despesa
    E escolhe o lançamento de número "1"
    E informa a nova categoria ""
    E informa o novo valor "150"
    Então o sistema deve exibir a mensagem "A categoria é obrigatória"
    E o lançamento deve permanecer com categoria "Comida" e valor R$ 100,00
