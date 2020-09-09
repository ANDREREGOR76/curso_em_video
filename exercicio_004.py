entrada = input('Digite algo: ')

if type(entrada) is str:
    print("O tipo primitivo desse valor é 'string'!")
elif type(entrada) is int:
    print("O tipo desse valor é 'inteiro'!")
elif type(entrada) is float:
    print("O tipo primitivo desse valor é 'ponto flutuante'!")
else:
    print("O tipo primitivo desse valor é 'booleano'!")

print('Só tem espacos? {}'.format(entrada.isspace()))
print('É um número? {}'.format(entrada.isnumeric()))
print('É alfabético? {}'.format(entrada.isalpha()))
print('É alfanumérico? {}'.format(entrada.isalnum()))
print('Está em maiúsculas? {}'.format(entrada.isupper()))
print('Está em minúsculas? {}'.format(entrada.islower()))
print('Está capitalizada? {}'.format(entrada.istitle()))
