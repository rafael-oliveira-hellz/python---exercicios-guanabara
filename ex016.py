import math
# import random
# import emoji

# num = int(input('Digite um número: '))
# raiz = math.sqrt(num)

# n = random.randint(1, 10)

# print('A raiz quadrada de {} é {:.3f}.'.format(num, raiz))
# print('O número aleatório é {}.'.format(n))
# print(emoji.emojize(':envelope:: '))
# print(emoji.emojize(':key:: '))

## Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

num = float(input('Digite um número: '))

real_num = math.trunc(num)

print(f'O valor digitado foi {num} e sua porção inteira é {real_num}.')
