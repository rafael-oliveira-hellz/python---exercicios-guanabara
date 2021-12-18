## Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite o seu nome: ')).lower().title().strip()

print('Silva' in nome)