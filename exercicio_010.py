"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
Considere
U$$ 1,00 = R$ 3,27
"""

valor_dolar = 3.27
carteira = float(input('Digite o valor que você tem na carteira: '))
carteira_em_dolar = carteira / valor_dolar
print('Com R${:.2f} você pode comprar U$${:.2f}.'.format(carteira, carteira_em_dolar))
