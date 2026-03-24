numero = input('escreva um número de 0 a 9999 ').zfill(4)

milhar = numero[0]
centena = numero[1]
dezena = numero[2]
unidade = numero[3]

print("Milhar:", milhar)
print("Centena:", centena)
print("Dezena:", dezena)
print("Unidade:", unidade)
