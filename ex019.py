'''import random
aluno1 = random.choice(str(input("Digite o nome do aluno: ")))
aluno2 = random.choice(str(input("Digite o nome do aluno: ")))
aleat = random.shuffle
print(f'O aluno escolhido foi {aleat}')
# falhei'''

from random import choice
n1 = input('primeiro aluno: ')
n2 = input('segundo aluno: ')
n3 = input('terceiro aluno: ')
n4 = input('quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f'o aluno escolhido foi {escolhido}')
