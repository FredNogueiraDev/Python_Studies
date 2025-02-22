nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

try:
	idade = int(idade)
except:
	idade = input('Idade deve ser um número: ')

print(f'Seu nome é {nome.upper()} e sua idade é {idade}.')

#-------------------------------
#valor_produto = float(input('Digite o valor do produto para aumentar 10%: R$'))

#valor_produto = valor_produto * 1.10

#print(f'R${valor_produto:.2f}')

