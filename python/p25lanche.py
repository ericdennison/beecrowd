# Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

# Entrada
# O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

# Saída
# O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.


codigo, quantidade = map(int, input().split(' '))

match codigo:
    case 1:
        cachorro_quente = quantidade * 4.00
        print(f'Total: R$ {cachorro_quente:.2f}')
    case 2:
        x_salada = quantidade * 4.50
        print(f'Total: R$ {x_salada:.2f}')
    case 3:
        x_bacon = quantidade * 5.00
        print(f'Total: R$ {x_bacon:.2f}')
    case 4:
        torrada_simples = quantidade * 2.00
        print(f'Total: R$ {torrada_simples:.2f}')
    case 5:
        refrigerante = quantidade * 1.50
        print(f'Total: R$ {refrigerante:.2f}')



    
        