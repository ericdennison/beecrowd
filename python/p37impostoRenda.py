'''
Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos, pois sabem que nele não existem políticos corruptos e os recursos arrecadados são utilizados em benefício da população, sem qualquer desvio. A moeda deste país é o Rombus, cujo símbolo é o R$.

Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. Em seguida, calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda, segundo a tabela abaixo.

Lembre que, se o salário for R$ 3002.00, a taxa que incide é de 8% apenas sobre R$ 1000.00, pois a faixa de salário que fica de R$ 0.00 até R$ 2000.00 é isenta de Imposto de Renda. No exemplo fornecido (abaixo), a taxa é de 8% sobre R$ 1000.00 + 18% sobre R$ 2.00, o que resulta em R$ 80.36 no total. O valor deve ser impresso com duas casas decimais.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima o texto "R$" seguido de um espaço e do valor total devido de Imposto de Renda, com duas casas após o ponto. Se o valor de entrada for menor ou igual a 2000, deverá ser impressa a mensagem "Isento".




'''

valor = float(input())

if valor > 4500:

    r = ((valor - 4500)/ 100)*28
    r1 = ((4500.00 - 3000.01) / 100) *18
    r2 = ((3000.00 - 2000.01)/ 100) * 8
    r3 = r + r1 + r2
    print(f'R$ {r3:.2f}')


elif valor >= 3000.01 and valor <= 4500.00:

    r1 = ((valor - 3000.01) / 100) *18
    r2 = ((3000.00 - 2000.01)/ 100) * 8
    r3 = r1 + r2
    print(f'R$ {r3:.2f}')

elif valor >= 2000.01 and valor <= 3000.00:

    r2 = ((valor - 2000.01)/ 100) * 8
    print(f'R$ {r2:.2f}')

elif valor >= 0.00 and valor <= 2000.00:
    print('Isento')






