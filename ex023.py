## Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = str(input('Digite um número de 0 a 9999: '))

print('\nO número digitado foi: {}'.format(num))
print('Sua unidade é: {}'.format(num[3]))
print('Sua dezena é: {}'.format(num[2]))
print('Sua centena é: {}'.format(num[1]))
print('seu milhar é: {}'.format(num[0]))