# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula

# Entrada
# O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.
import math

x1,y1 = map(float,input().split(' '))
x2,y2 = map(float,input().split(' '))
distancia = math.sqrt(((x2 - x1)**2)+((y2 - y1)**2))
print(f'{distancia:.4f}')