'''
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:

se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

'''

x,y,z = map(float, input().split(' '))

if x > y and x > z and y > z or x == y and y == z:
    a = x
    b = y
    c = z
    print(a, b, c)

elif x > y and x > z and y < z:
    a = x
    b = z
    c = y
    print(a, b, c)

elif x < y and x < z and y > z:
    a = y
    b = z
    c = x
    print(a, b, c)

elif x == y and x < z and y < z:
    a = z
    b = x
    c = y 
    print(a, b, c)