# language: pt
Como usuário do sistema de gestão de gastos pessoais 
Quero registrar minhas despesas 
Para acompanhar quanto gasto por categoria 

Cenário: Registrar despesa com sucesso 
    Dado que o usuário executou a aplicação no terminal 
    E que o menu principal está sendo exibido 
    Quando o usuário seleciona a opção "1" de registrar despesa 
    E informa a categoria "Comida" 
    E informa o valor "1000"
    Então o sistema deve registrar a despesa com categoria "Comida" e valor R$ 1000,00 
    E deve exibir a mensagem "Despesa registrada com sucesso" 
    E deve retornar ao menu principal

Cenário: Valor não numérico 
	Dado que o usuário executou a aplicação no terminal 
    E que o menu principal está sendo exibido 
    Quando o usuário seleciona a opção "1" de registrar despesa 
    E informa a categoria "Comida" E informa o valor "abc" 
    Então o sistema deve exibir a mensagem "Valor inválido"
    E não deve registrar nenhuma despesa 

Cenário: Valor zero ou negativo 
	Dado que o usuário executou a aplicação no terminal 
    E que o menu principal está sendo exibido 
    Quando o usuário seleciona a opção "1" de registrar despesa 
    E informa a categoria "Comida" 
    E informa o valor "-50" 
    Então o sistema deve exibir a mensagem "O valor deve ser maior que zero" 
    E não deve registrar nenhuma despesa 

Cenário: Categoria vazia 
	Dado que o usuário executou a aplicação no terminal 
    E que o menu principal está sendo exibido 
    Quando o usuário seleciona a opção "1" de registrar despesa 
    E informa a categoria ""
    E informa o valor "100" 
    Então o sistema deve exibir a mensagem "A categoria é obrigatória" 
    E não deve registrar nenhuma despesa 
