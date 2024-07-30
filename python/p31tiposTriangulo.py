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
lista = [x, y, z]
lista.sort(reverse=True)
a,b,c = lista

if a >= (b + c):
    print('NAO FORMA TRIANGULO')

    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b != c or a != b == c:
        print('TRIANGULO ISOSCELES')

elif a**2 == ((b**2)+(c**2)):
    print('TRIANGULO RETANGULO')

    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b != c or a != b == c:
        print('TRIANGULO ISOSCELES')

elif a**2 > ((b**2)+(c**2)):
    print('TRIANGULO OBTUSANGULO')

    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b != c or a != b == c:
        print('TRIANGULO ISOSCELES')

elif a**2 < ((b**2)+(c**2)):
    print('TRIANGULO ACUTANGULO')

    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b != c or a != b == c:
        print('TRIANGULO ISOSCELES')
