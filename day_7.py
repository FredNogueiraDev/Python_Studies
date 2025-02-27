# # FOR LOOPŚ
# for n in range(100):
#     print(n)

nome = 'FREDERICO'
vowels = ['A', 'E', 'I', 'O', 'U']

# for letter in nome:
#     if(vowels.__contains__(letter)):
#         print(letter)

# nome_com_espacos = ''
#
# for letter in nome:
#     nome_com_espacos += f' {letter}'
#
# nome_com_espacos = nome_com_espacos[1:]
# print(nome_com_espacos)
#
# # SOLUÇÃO DO PROFESSOR:
# for letter in nome:
#     print(f' {letter}', end='')

# RETANGULO
# text = ''
# for l in range(6*6):
#     text+='@'
#     if(len(text) == 6):
#         print(text)
#         text = ''

#
# for l in range(6):
#     for c in range(6):
#         print('@', end='')
#     print('')

max_valor = 1000
min_valor = 500
valor = min_valor

while valor <= max_valor:
    print(f'R${valor}')
    valor += 50