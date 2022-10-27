"""
Crie uma calculadora com while
"""
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite o outro número: ')
    operador = input('Digite um operador: ')

    numeros_sao_validos = None
    numero_1_float = 0
    numero_2_float = 0

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_sao_validos = True
    except:
        numeros_sao_validos = None

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador não é válido')
        continue

    if operador == '+':
        print(f'Resultado = {numero_1_float + numero_2_float}')

    quer_sair = input('Quer [s]air? ').lower().startswith('s')

    if quer_sair:
        break
