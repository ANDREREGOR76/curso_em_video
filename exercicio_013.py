"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário
com 15% de aumento.
"""

salario = float(input('Digite o valor do seu salário: '))
print(
    'Parabéns!\nComo reconhecimento ao excelente trabalho que você vem desenvolvendo, você recebeu um aumento.'
    '\nSeu salário agora é de R${:.2f}!'.format(salario * 1.15))
