'''
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.
'''

lista_valores = []
contador = 0
valores_positivos = 0

lista_valores.append(float(input()))
lista_valores.append(float(input()))
lista_valores.append(float(input()))
lista_valores.append(float(input()))
lista_valores.append(float(input()))
lista_valores.append(float(input()))

while contador < len(lista_valores):
    if lista_valores[contador] > 0:
        valores_positivos += 1

    contador += 1
print(f'{valores_positivos} valores positivos')