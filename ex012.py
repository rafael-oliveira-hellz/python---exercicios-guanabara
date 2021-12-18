## Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

raw_price = float(input('Digite o valor do produto: R$'))
discount = 5 / 100

off_price = raw_price - (raw_price * discount)

print(f'O valor do produto é: R${raw_price}.')
print(f'O valor do desconto é: R${discount}.')
print(f'O valor do produto com desconto é: R${off_price}.')