# Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


# Perimetro = XX.X


# Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


# Area = XX.X

a,b,c = map(float,input().split(' '))

a_true = (b - c) < a < (b + c)
b_true = (a - c) < b < (a + c)
c_true = (a - b) < c < (a + b)

if a_true and b_true and c_true:
    perimetro = a + b + c
    print(f'Perimetro = {perimetro:.1f}')
else:
    area = ((a+b)*c)/2
    print(f'Area = {area:.1f}')
