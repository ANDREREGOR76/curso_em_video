"""
Faça um programa que leia um ângulo qualquer e mostre na tela
o valor do seno, cosseno e tangente desse ângulo.
"""


from math import radians, sin, cos, tan

ang = float(input('Digite o valor do ângulo: '))
print(
    'Seno de {}: {:.2f}\n'
    'Cosseno de {}: {:.2f}\n'
    'Tangente de {}: {:.2f}'.format(
        ang, sin(radians(ang)), ang, cos(radians(ang)), ang, tan(radians(ang))
    )
)