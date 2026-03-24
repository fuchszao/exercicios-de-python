letra = input('escreve qualquer merda ai: ').lower().strip()

print(f'quantas vezes aparece a letra a: {letra.count('a')}')
print(f'posição que aparece a letra a primeiro: {letra.find('a')}')
print(f'agora ultima posição da letra a: {letra.rfind('a')}')
