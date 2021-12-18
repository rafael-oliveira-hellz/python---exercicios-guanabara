## Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
# A = W x H

width = float(input('Digite a largura da parede em metros: '))
height = float(input('Digite a altura da parede em metros: '))

area = width * height

painting = area / 2

print(f'A largura da parede é: {width}m².')
print(f'A altura da parede é: {height}m².')
print(f'A área a ser pintada é: {area}m².\n')
print(f'Será necessário {painting} litros de tinta para pintar a parede.')


