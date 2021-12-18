## Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e
# todas as informações possíveis sobre ele.

dado = input('Digite algo: ')

print('Qual seu tipo primitivo?', type(dado))
print('É alfabético? ', dado.isalpha())
print('É alfanumérico? ', dado.isalnum())
print('Só tem espaços? ', dado.isspace())
print('Só tem números? ', dado.isdigit())
print('Está capitalizado? ', dado.istitle())
print('É tudo minúscula? ', dado.islower())
print('É tudo maiúscula? ', dado.isupper())
