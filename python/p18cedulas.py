# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

inteiro = int(input())

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

print(inteiro)
print(f'{valor100q} nota(s) de R$ 100,00')
print(f'{valor50q} nota(s) de R$ 50,00')
print(f'{valor20q} nota(s) de R$ 20,00')
print(f'{valor10q} nota(s) de R$ 10,00')
print(f'{valor5q} nota(s) de R$ 5,00')
print(f'{valor2q} nota(s) de R$ 2,00')
print(f'{valor1q} nota(s) de R$ 1,00')

