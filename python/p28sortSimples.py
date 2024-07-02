# Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

a,b,c= map(int, input().split(' '))
lista = [a,b,c]
lista_ordenada = sorted(lista)

for i in lista_ordenada:
    print(i)
print()
for j in lista:
    print(j)