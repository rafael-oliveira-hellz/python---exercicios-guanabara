## Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
# mostre o comprimento da hipotenusa.
# hipotenusa = catetooposto² + catetoadjacente²

from math import hypot

co =  float(input('Digite o valor do Cateto Oposto: '))
ca =  float(input('Digite o valor do Cateto Adjacente: '))

hipotenusa = hypot(co, ca)

print('A hipotenusa mede {:.2f}.'.format(hipotenusa))