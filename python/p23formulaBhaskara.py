import math
# Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

try:
    a,b,c = map(float, input().split(' '))
    delta = ((b**2)-(4*a*c))

    raiz_1 = 0
    raiz_2 = 0
    raiz_1= math.sqrt(delta)
    raiz_2= math.sqrt(delta)
 
    r1 = (-b + (raiz_1))/(2*a)
    r2 = (-b - (raiz_2))/(2*a)
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')

except:
    print('Impossivel calcular')
