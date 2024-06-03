# Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
# a) a área do triângulo retângulo que tem A por base e C por altura.
# b) a área do círculo de raio C. (pi = 3.14159)
# c) a área do trapézio que tem A e B por bases e C por altura.
# d) a área do quadrado que tem lado B.
# e) a área do retângulo que tem lados A e B.

a,b,c = map(float,input().split(' '))
pi = 3.14159

aT = ((a*c)/2)
aC = pi*(c**2)
aTr = ((a+b)*c)/2
aQ = b**2
aR = a*b

print(f'TRIANGULO: {aT:.3f}')
print(f'CIRCULO: {aC:.3f}')
print(f'TRAPEZIO: {aTr:.3f}')
print(f'QUADRADO: {aQ:.3f}')
print(f'RETANGULO: {aR:.3f}')
