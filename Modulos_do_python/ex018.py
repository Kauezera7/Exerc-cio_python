import math
ang = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('O ângulo de {:.0f} tem o SENO de {:.2f}'.format(ang, seno))
print(f'Oângulo de {ang:.0f} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de  {ang:.0f} tem a TANGENTE de {tangente:.2f}')