## Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = int(input('Quantos KM foram percorridos? '))
days = int(input('Por quantos dias o carro foi alugado? '))

price_km = km * 0.15
price_days = days * 60

total_price = price_days + price_km

print(f'O valor total a pagar é de R${total_price}')