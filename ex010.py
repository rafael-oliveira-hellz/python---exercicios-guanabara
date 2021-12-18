## Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
### US$ 1,00 BRL 3,27

brl = float(input('Quanto tem de dinheiro? '))

dolar = brl / 3.27

print('Você tem R${:.2f} e consegue comprar US${:.2f}'.format(brl, dolar))
