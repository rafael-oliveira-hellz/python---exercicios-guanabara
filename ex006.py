## Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt

num = float(input('Digite um número: '))

print('O número digitado é: {:.0f}, seu dobro é {:.0f} e sua raiz quadrada é {:.3f}.'.format(num, num * 2, sqrt(num)))
