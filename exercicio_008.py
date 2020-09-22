"""
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

valor_metros = float(input('Digite uma medida em metros: '))
print('{} metros equivale a {} centímetros e a {} milímetros.'.format(valor_metros, valor_metros*100, valor_metros*1000))
