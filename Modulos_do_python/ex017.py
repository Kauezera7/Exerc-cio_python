#from math import hypot#
import math
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente  = float(input('Comprimento do cateto adjacente:'))
#hipotenusa = hypot(cateto_oposto, cateto_adjacente)
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print('A hipotenusa vai medir {:.2f}.'.format(hipotenusa))