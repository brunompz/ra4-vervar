# language: pt
Funcionalidade: Definir orçamento do mês
    Como usuário do sistema de gestão de gastos pessoais
    Quero definir um orçamento para o mês
    Para controlar quanto posso gastar

Cenário: Definir orçamento com sucesso
    Dado que o usuário executou a aplicação no terminal
    E que o menu principal está sendo exibido
    Quando o usuário seleciona a opção "6" de definir orçamento
    E informa o valor "2000"
    Então o sistema deve registrar o orçamento de R$ 2000,00
    E deve exibir a mensagem "Orçamento definido com sucesso"
    E deve retornar ao menu principal

Cenário: Redefinir orçamento já existente
    Dado que o usuário executou a aplicação no terminal
    E existe um orçamento definido de R$ 2000,00
    Quando o usuário seleciona a opção "6" de definir orçamento
    E informa o valor "3000"
    Então o sistema deve substituir o orçamento por R$ 3000,00

Cenário: Valor não numérico
    Dado que o usuário executou a aplicação no terminal
    Quando o usuário seleciona a opção "6" de definir orçamento
    E informa o valor "abc"
    Então o sistema deve exibir a mensagem "Valor inválido"
    E não deve definir nenhum orçamento

Cenário: Valor negativo ou zero
    Dado que o usuário executou a aplicação no terminal
    Quando o usuário seleciona a opção "6" de definir orçamento
    E informa o valor "-100"
    Então o sistema deve exibir a mensagem "O valor deve ser maior que zero"
    E não deve definir nenhum orçamento

Cenário: Valor vazio
    Dado que o usuário executou a aplicação no terminal
    Quando o usuário seleciona a opção "6" de definir orçamento
    E informa o valor ""
    Então o sistema deve exibir a mensagem "O valor é obrigatório"
    E não deve definir nenhum orçamento
