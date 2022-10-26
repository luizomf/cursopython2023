"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
from curses.ascii import isdigit
from re import L

numero_str = input('Digite um número: ')

try:
    print('STR:', numero_str, type(numero_str))
    numero_int = int(numero_str)
    print('INT:', numero_int, type(numero_int))
    print(numero_int * 3)
except:
    print('Isso não é um número')

# if numero_str.isdigit():
#     print('STR:', numero_str, type(numero_str))
#     numero_int = int(numero_str)
#     print('INT:', numero_int, type(numero_int))
#     print(numero_int * 3)
# else:
#     print('Isso não é um número')
