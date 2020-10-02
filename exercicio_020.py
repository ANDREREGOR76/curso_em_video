"""
O professor quer sortear a ordem de apresentação de trabalhos dos seus quatro alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""


from random import shuffle

aluno_1 = input('Aluno 1: ')
aluno_2 = input('Aluno 2: ')
aluno_3 = input('Aluno 3: ')
aluno_4 = input('Aluno 4: ')

alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
shuffle(alunos)
print('A ordem sorteada para a apresentação dos trabalhos foi:')
for aluno in alunos:
    print(aluno, '', end='')
