'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.
'''

h_i,m_i,h_f,m_f = map(int, input().split(' '))

min_i = (h_i * 60) + m_i
min_f = (h_f * 60) + m_f

if  min_f >= min_i:

    d_m = min_f - min_i
    
    if d_m == 0:
        d_m = d_m + (24 * 60)

else:

    d_m = ((24 * 60) - min_i) + min_f


horas = d_m // 60
minutos = d_m % 60

print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')