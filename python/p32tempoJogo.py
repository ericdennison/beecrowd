'''
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.
'''

inicial,final = map(int, input().split(' '))

if final > inicial:
    duracao = final - inicial
    print(f'O JOGO DUROU {duracao} HORA(S)')
else:
    duracao = (24 - inicial) + final
    print(f'O JOGO DUROU {duracao} HORA(S)')

