dias = float(input('qual a quantidade de dias que o carro foi alugado? '))
km = float(input('quantos km o carro foi rodado? '))
custo = (dias * 60) + (km * 0.15)
print(f'o custo do aluguel do carro foi de R${custo:.2f}')
