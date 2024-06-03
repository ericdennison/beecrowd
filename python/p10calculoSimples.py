# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

cp,np,vup = map(float,input().split(' '))
cp2,np2,vup2 = map(float,input().split(' '))
vt = (vup*np)+(vup2*np2)
print(f'VALOR A PAGAR: R$ {vt:.2f}')