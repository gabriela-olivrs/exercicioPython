import math

co = float(input('Cateto Oposto:'))
ca = float(input('Cateto adjacente'))
h = math.sqrt(pow(co, 2) + pow(ca, 2))
print('hipotenusa: {:0.02f}'.format(h))

# h2 = co2+ ca2 ou math.hypot(co, ca)
