#language: pt
Como usuário do sistema de gestão de gastos pessoais
Quero registrar minhas receitas 
Para saber quanto dinheiro entrou 

Cenário: Registrar receita com sucesso 
	Dado que o usuário executou a aplicação no terminal 
    E que o menu principal está sendo exibido 
    Quando o usuário seleciona a opção "2" de registrar receita 
    E informa a descrição "Salário" 
    E informa o valor "3000" 
    Então o sistema deve registrar a receita com descrição "Salário" e valor R$ 3000,00 
    E deve exibir a mensagem "Receita registrada com sucesso" 
    E deve retornar ao menu principal 

Cenário: Valor não numérico
	Dado que o usuário executou a aplicação no terminal 
    E que o menu principal está sendo exibido 
    Quando o usuário seleciona a opção "2" de registrar receita 
    E informa a descrição "Salário" 
    E informa o valor "abc" 
    Então o sistema deve exibir a mensagem "Valor inválido" 
    E não deve registrar nenhuma receita 

Cenário: Valor zero ou negativo 
    Dado que o usuário executou a aplicação no terminal 
    E que o menu principal está sendo exibido 
    Quando o usuário seleciona a opção "2" de registrar receita 
    E informa a descrição "Freela" 
    E informa o valor "0" 
    Então o sistema deve exibir a mensagem "O valor deve ser maior que zero" 
    E não deve registrar nenhuma receita 

Cenário: Descrição vazia 
	Dado que o usuário executou a aplicação no terminal 
    E que o menu principal está sendo exibido 
    Quando o usuário seleciona a opção "2" de registrar receita 
    E informa a descrição "" 
    Então o sistema deve exibir a mensagem "A descrição é obrigatória" 
    E não deve permitir o usuário prosseguir para a etapa de valor
