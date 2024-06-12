# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

# Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

idade = int(input())
anos = 0
meses = 0
dias = 0

if idade >= 365:
    while idade >= 365:
        idade = idade - 365
        anos = anos + 1
        
    if idade < 365 and idade >= 30:    
        while idade  >=  30:
            idade = idade - 30
            meses = meses + 1
            
        if idade < 30 and idade >= 0:
            dias = idade
elif idade < 365:
        while idade  >=  30:
            idade = idade - 30
            meses = meses + 1
            
        if idade < 30 and idade >= 0:
            dias = idade

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')
