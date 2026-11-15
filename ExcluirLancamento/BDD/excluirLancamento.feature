# language: pt
Funcionalidade: Excluir lançamento
    Como usuário do sistema de gestão de gastos pessoais
    Quero excluir um lançamento já registrado
    Para remover registros feitos por engano

Cenário: Excluir lançamento com sucesso
    Dado que o usuário executou a aplicação no terminal
    E existe uma despesa registrada com categoria "Comida" e valor R$ 100,00
    Quando o usuário seleciona a opção "7" de excluir lançamento
    E escolhe o tipo "1" de despesa
    E escolhe o lançamento de número "1"
    Então o sistema deve remover o lançamento
    E deve exibir a mensagem "Lançamento excluído com sucesso"
    E deve retornar ao menu principal

Cenário: Excluir lançamento inexistente
    Dado que o usuário executou a aplicação no terminal
    E não existem despesas registradas
    Quando o usuário seleciona a opção "7" de excluir lançamento
    E escolhe o tipo "1" de despesa
    E escolhe o lançamento de número "1"
    Então o sistema deve exibir a mensagem "Lançamento não encontrado"
    E deve retornar ao menu principal

Cenário: Excluir lançamento não afeta os demais
    Dado que o usuário executou a aplicação no terminal
    E existe uma despesa registrada com categoria "Comida" e valor R$ 100,00
    E existe uma despesa registrada com categoria "Lazer" e valor R$ 50,00
    Quando o usuário seleciona a opção "7" de excluir lançamento
    E escolhe o tipo "1" de despesa
    E escolhe o lançamento de número "1"
    Então a despesa com categoria "Lazer" e valor R$ 50,00 deve continuar registrada
