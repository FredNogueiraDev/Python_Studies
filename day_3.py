mensagem = 'Essa mensagem só tem 1 linha'
mensagem_2 = """Essa mensagem
 tem mais de 
 uma linha """

print(mensagem)
print(mensagem_2)
print(mensagem[0])
print(mensagem[0:3])
print(len(mensagem))
print(mensagem.upper())
print(mensagem.lower())
print(mensagem.replace('linha', 'frase'))


nome = 'fred'
idade = 21

print (f'meu nome é {nome} e tenho {idade} anos')