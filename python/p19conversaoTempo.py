# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

inteiro = int(input())
horas = inteiro//3600
minutos = (inteiro % 3600) // 60
segundos = inteiro % 60
print(f'{horas}:{minutos}:{segundos}')