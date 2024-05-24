# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

num = int(input())
ht = int(input())
vht = float(input())
sal = ht * vht
print(f'NUMBER = {num}')
print(f'SALARY = U$ {sal:.2f}')