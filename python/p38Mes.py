
'''
Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

Entrada
A entrada contém um único valor inteiro.

Saída
Imprima por extenso o nome do mês correspondente ao número existente na entrada, com a primeira letra em maiúscula.
'''
valor = int(input())

if valor == 1:
    print('January')
elif valor == 2:
    print('February')
elif valor == 3:
    print('March')
elif valor == 4:
    print('April')
elif valor == 5:
    print('May')
elif valor == 6:
    print('June')
elif valor == 7:
    print('July')
elif valor == 8:
    print('August')
elif valor == 9:
    print('September')
elif valor == 10:
    print('October')
elif valor == 11:
    print('November')
elif valor == 12:
    print('December')