'''

A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salário	
0 - 400.00
400.01 - 800.00
800.01 - 1200.00
1200.01 - 2000.00
Acima de 2000.00

Percentual de Reajuste
15%
12%
10%
7%
4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

'''

salario = float(input())

if salario >= 0 and salario <= 400.00:
    PERCENTUAL = 15
    reajuste = ((salario/100)*PERCENTUAL)
    novo_salario = salario + reajuste

    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: {PERCENTUAL} %')

elif salario >= 400.01 and salario <= 800.00:
    PERCENTUAL = 12
    reajuste = ((salario/100)*PERCENTUAL)
    novo_salario = salario + reajuste

    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: {PERCENTUAL} %')

elif salario >= 800.01 and salario <= 1200.00:
    PERCENTUAL = 10
    reajuste = ((salario/100)*PERCENTUAL)
    novo_salario = salario + reajuste

    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: {PERCENTUAL} %')

elif salario >= 1200.01 and salario <= 2000.00:
    PERCENTUAL = 7
    reajuste = ((salario/100)*PERCENTUAL)
    novo_salario = salario + reajuste

    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: {PERCENTUAL} %')

else:

    PERCENTUAL = 4
    reajuste = ((salario/100)*PERCENTUAL)
    novo_salario = salario + reajuste

    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: {PERCENTUAL} %')

