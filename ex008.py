##  Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

mts = float(input('Digite um valor em metros'))

cm = mts * 100
mm = mts * 1000

print('{} metros, {} cm, {} mm'.format(mts, cm, mm))
