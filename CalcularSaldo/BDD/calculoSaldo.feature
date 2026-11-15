# language: pt
Funcionalidade: Cálculo de saldo
    Como usuário do sistema de gestão de gastos pessoais
    Quero calcular o meu saldo atual
    Para saber quanto dinheiro tenho disponível no mês considerando lançamentos normais e recorrentes já ocorridos

Cenário: Calcular saldo positivo com sucesso
    Dado que o usuário executou a aplicação no terminal
    E existem receitas registradas totalizando R$ 3000,00
    E existem despesas registradas totalizando R$ 1000,00
    Quando o usuário seleciona a opção "5" de calcular saldo
    Então o sistema deve exibir o saldo de R$ 2000,00
    E deve retornar ao menu principal

Cenário: Calcular saldo negativo
    Dado que o usuário executou a aplicação no terminal
    E existem receitas registradas totalizando R$ 1000,00
    E existem despesas registradas totalizando R$ 1500,00
    Quando o usuário seleciona a opção "5" de calcular saldo
    Então o sistema deve exibir o saldo de R$ -500,00
    E deve retornar ao menu principal

Cenário: Calcular saldo zerado
    Dado que o usuário executou a aplicação no terminal
    E existem receitas registradas totalizando R$ 1000,00
    E existem despesas registradas totalizando R$ 1000,00
    Quando o usuário seleciona a opção "5" de calcular saldo
    Então o sistema deve exibir o saldo de R$ 0,00
    E deve retornar ao menu principal

Cenário: Calcular saldo incluindo recorrentes com dia já atingido no mês
    Dado que o usuário executou a aplicação no terminal
    E que o dia atual do mês é "10"
    E existe uma receita registrada de R$ 1000,00
    E existe uma receita recorrente mensal de R$ 3000,00 para o dia "05"
    E existe uma despesa registrada de R$ 500,00
    E existe uma despesa recorrente mensal de R$ 250,00 para o dia "10"
    Quando o usuário seleciona a opção "5" de calcular saldo
    Então o sistema deve exibir o saldo de R$ 3250,00
    E deve retornar ao menu principal

Cenário: Calcular saldo desconsiderando recorrentes com dia futuro no mês
    Dado que o usuário executou a aplicação no terminal
    E que o dia atual do mês é "05"
    E existe uma receita registrada de R$ 1000,00
    E existe uma receita recorrente mensal de R$ 3000,00 para o dia "20"
    E existe uma despesa registrada de R$ 400,00
    E existe uma despesa recorrente mensal de R$ 250,00 para o dia "15"
    Quando o usuário seleciona a opção "5" de calcular saldo
    Então o sistema deve exibir o saldo de R$ 600,00
    E deve retornar ao menu principal

Cenário: Calcular saldo sem lançamentos registrados
    Dado que o usuário executou a aplicação no terminal
    E não existem receitas nem despesas registradas
    Quando o usuário seleciona a opção "5" de calcular saldo
    Então o sistema deve exibir o saldo de R$ 0,00
    E deve exibir a mensagem "Nenhum lançamento registrado"
    E deve retornar ao menu principal
