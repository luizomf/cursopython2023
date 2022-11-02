# Manipulando chaves e valores em dicionários
from pprint import pprint


def p(dicionario):
    pprint(dicionario, sort_dicts=False)


pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
pessoa['nome'] = 'João'
pessoa[(1, 2, 3)] = 'EITA'
del pessoa[(1, 2, 3)]
del pessoa['nome']
del pessoa['endereços']
pessoa['teste de atenção'] = 'ATENÇÃO'
print(pessoa['teste de atenção'])
pessoa['teste de atenção'] = 'NOVA ATENÇÃO'
del pessoa['teste de atenção']
p(pessoa)

# for chave in pessoa:
#     if isinstance(chave, tuple):
#         for valor in chave:
#             print(valor, '<<-- DA TUPLA')

# chave_dinamica = 'nome'
# # print(pessoa[chave_dinamica])

# if pessoa.get(chave_dinamica) is None:
#     print('Chave não existe')
# else:
#     print(pessoa.get(chave_dinamica))

# print(pessoa.get(chave_dinamica))
