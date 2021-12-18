## Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import cos, radians, sin, tan


angle = float(input('Digite o ângulo desejado: '))

sin = sin(radians(angle))
cos = cos(radians(angle))
tan = tan(radians(angle))

print('\nO ângulo de {} tem o SENO de {:.2f}.'.format(angle, sin))
print('O ângulo de {} tem o COSSENO de {:.2f}.'.format(angle, cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}.'.format(angle, tan))