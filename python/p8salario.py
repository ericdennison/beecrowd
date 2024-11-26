# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

numero_funcionario = int(input())
horas_trabalhadas = int(input())
valor_horas_trabalhadas = float(input())
salalario = horas_trabalhadas * valor_horas_trabalhadas
print(f'NUMBER = {numero_funcionario}')
print(f'SALARY = U$ {salalario:.2f}')