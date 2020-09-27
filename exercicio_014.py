"""
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
"""
cels = float(input('Digite a temperatura em Celsius: '))
print('{} graus Celsius equivale a {:.1f} graus Fahrenheit.'.format(cels, ((cels * 9) / 5) + 32))
