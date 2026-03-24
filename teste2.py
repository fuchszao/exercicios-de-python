n1 = int(input('qual sua idade? '))
if n1 <= 14:
    print('tu é kid')
if n1 < 18 and n1 > 14:
    print('tu é adolescente')
if n1 >= 18 and n1 < 60:
    print('tu é adulto')
if n1 >= 60:
    print('tu ta véi pa carai')