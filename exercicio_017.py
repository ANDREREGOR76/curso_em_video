"""
Faça um programa que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo retângulo, calcule e mostre
o comprimento da hipotenusa.
"""

from math import hypot

cat_op = float(input('Valor do cateto oposto: '))
cat_ad = float(input('Valor do cateto adjacente: '))
print('O comprimento da hipotenusa é {}.'.format(hypot(cat_op, cat_ad)))
print('O comprimento da hipotenusa é {}.'.format(((cat_op**2) + (cat_ad**2)) ** 0.5))
