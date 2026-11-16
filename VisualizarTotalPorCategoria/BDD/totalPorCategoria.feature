# language: pt
Funcionalidade: Visualizar total por categoria
    Como usuário do sistema de gestão de gastos pessoais
    Quero visualizar o total gasto em cada categoria
    Para saber onde estou gastando mais

Cenário: Exibir total de uma categoria
    Dado que o usuário executou a aplicação no terminal
    E existe uma despesa "Comida" de R$ 300,00
    Quando o usuário seleciona a opção "7" de total por categoria
    Então o sistema deve exibir "Comida: R$ 300,00"
    E deve retornar ao menu principal

Cenário: Somar despesas da mesma categoria
    Dado que o usuário executou a aplicação no terminal
    E existe uma despesa "Comida" de R$ 300,00
    E existe uma despesa "Comida" de R$ 200,00
    Quando o usuário seleciona a opção "7" de total por categoria
    Então o sistema deve exibir "Comida: R$ 500,00"

Cenário: Exibir totais de várias categorias
    Dado que o usuário executou a aplicação no terminal
    E existe uma despesa "Comida" de R$ 300,00
    E existe uma despesa "Transporte" de R$ 100,00
    Quando o usuário seleciona a opção "7" de total por categoria
    Então o sistema deve exibir "Comida: R$ 300,00"
    E deve exibir "Transporte: R$ 100,00"

Cenário: Sem lançamentos registrados
    Dado que o usuário executou a aplicação no terminal
    E não existem despesas registradas
    Quando o usuário seleciona a opção "7" de total por categoria
    Então o sistema deve exibir a mensagem "Nenhum lançamento registrado"
    E deve retornar ao menu principal
