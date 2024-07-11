'''
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

'''


a,b = map(int,input().split(' '))

if a < b :
    resto = b % a
    if resto == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
elif a > b:
    resto = a % b
    if resto == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
