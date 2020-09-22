"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

preco = float(input('informe o valor do produto: '))
preco_com_desconto = preco * 0.95
print(
    'Você tem direito a um desconto! O produto que você quer levar sairá por apenas R${:.2f}.'
        .format(preco_com_desconto))
