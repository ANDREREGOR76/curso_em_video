"""
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 m².
"""

print('Informe as medidas em metros da parede que você quer pintar!')
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2
print()
print('A sua parede tem {}m² de área.'.format(area))
print('Para pintar uma parede com essa área, será(ão) necessário(s) {:.2f} litro(s) de tinta.'.format(tinta))
