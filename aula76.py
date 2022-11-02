# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}

# p1.update({
#     'nome1': 'AAAA',
#     'sobrenome1': 'BBBB',
#     'idade': 123,
# })
# p1.update(idade=123, nome='Qualquer outro')
variavel = (1,)
print(variavel)
p1.update(
    (
        ('Chave', 'Valor'),
        ('Chave1', 'Valor1'),
        ('Chave2', 'Valor1'),
    )
)
print(p1)
# print(p1.get('nome', 'Valor padrão'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
