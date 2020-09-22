"""
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
"""

num = int(input('Você quer ver a tabuada de qual número? '))
print()
print('='*86)
for i in range(1, 11):
    print('{:<2} + {:>2} = {:>2}'.format(num, i, num + i), end='     ')
    print('||', end='     ')
    print('{:<2} - {:>2} = {:>2}'.format(num, i, num - i), end='     ')
    print('||', end='     ')
    print('{:<2} * {:>2} = {:>2}'.format(num, i, num * i), end='     ')
    print('||', end='     ')
    print('{:<2} / {:>2} = {:.2f}'.format(num, i, num / i))
print('='*86)
