## Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('\nDigite uma frase: ')).strip().lower()

#print('\nQuantidade de vezes que a letra ''A'' aparece: {}'.format(frase.count('A')))
print('\nQuantidade de vezes que a letra ''a'' aparece: {}'.format(frase.count('a')))

#print('\nEm que posição o A aparece a primeira vez: {}'.format(frase.find('A')))
print('Em que posição o a aparece a primeira vez: {}'.format(frase.find('a')+1))

#print('\nEm que posição o A aparece pela ultima vez: {}'.format(frase.rfind('A')))
print('Em que posição o a aparece pela ultima vez: {}'.format(frase.rfind('a')+1))