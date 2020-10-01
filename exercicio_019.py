"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""


import random
primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')

#Possibilidade 01
sorteado = random.randint(1, 4)
if sorteado == 1:
    print('O aluno escolhido foi {}.'.format(primeiro))
elif sorteado == 2:
    print('O aluno sorteado foi {}.'.format(segundo))
elif sorteado == 3:
    print('O aluno sorteado foi {}.'.format(terceiro))
else:
    print('O aluno sorteado foi {}.'.format(quarto))

#Possibilidade 02
lista = [primeiro, segundo, terceiro, quarto]
sorteado2 = random.choice(lista)
print('O aluno sorteado foi {}.'.format(sorteado2))
