import math
an = float(input('digite o ângulo que vc deseja: '))
seno =math.sin(math.radians(an))
print(f'o ângulo de {an} tem o seno de {seno:.2f}')
cosseno = math.cos(math.radians(an))
print(f'o ângulo de {an} tem o cosseno de {cosseno:.2f}')
tangente = math.tan(math.radians(an))
print(f'o ângulo de {an} tem a tangente de {tangente:.2f}')
