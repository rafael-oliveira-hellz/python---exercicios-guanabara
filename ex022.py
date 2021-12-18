# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
#  - Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: '))

print('Seu nome é: {}'.format(nome.upper()))
print('Seu nome é: {}'.format(nome.lower()))
print('Seu nome é: {}'.format(nome.strip().split(' ')[0]))
      