# Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

inteiro = float(input())

valor100 = inteiro % 100 
valor100q= inteiro // 100

valor50 = valor100 % 50
valor50q = valor100 // 50

valor20 = valor50 % 20
valor20q = valor50 // 20

valor10 = valor20 % 10
valor10q = valor20 // 10


valor5 = valor10 % 5
valor5q = valor10 // 5

valor2 = valor5 % 2
valor2q = valor5 // 2

valor1 = valor2 % 1
valor1q = valor2 // 1

valor050 = valor1 % 0.50
valor050q = valor1 // 0.50

valor025= valor050 % 0.25
valor025q = valor050 // 0.25

valor010 = valor025 % 0.10
valor010q = valor025 // 0.10

valor005 = valor010 % 0.05
valor005q = valor010 // 0.05

valor001 = valor005 % 0.01
valor001q = valor005 / 0.01

print('NOTAS:')
print(f'{valor100q:.0f} nota(s) de R$ 100.00')
print(f'{valor50q:.0f} nota(s) de R$ 50.00')
print(f'{valor20q:.0f} nota(s) de R$ 20.00')
print(f'{valor10q:.0f} nota(s) de R$ 10.00')
print(f'{valor5q:.0f} nota(s) de R$ 5.00')
print(f'{valor2q:.0f} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{valor1q:.0f} moeda(s) de R$ 1.00')
print(f'{valor050q:.0f} moeda(s) de R$ 0.50')
print(f'{valor025q:.0f} moeda(s) de R$ 0.25')
print(f'{valor010q:.0f} moeda(s) de R$ 0.10')
print(f'{valor005q:.0f} moeda(s) de R$ 0.05')
print(f'{round(valor001q)} moeda(s) de R$ 0.01')



