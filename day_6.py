# Exercício 1
#degress = int(input('Qual a temperatura do dia? '))

def temperature_control(degress):
    if degress < 10: return print('Muito frio')
    elif degress <= 25: return print('Está fresco')
    return print('Está quente')

#temperature_control(degress)

# Exercício 2
#hour = int(input('Quantas horas são? '))

def greeting(hour):
    if 24 < hour:
        return print('Isso não é uma hora válida')
    elif 4 < hour < 12:
        return print('Bom dia')
    elif 11 < hour < 18:
        return print('Boa tarde')
    return print('Boa noite')

#greeting(hour)

# Exercício 3

#purchase_value = int(input('Qual o valor da compra? R$'))

def calculate_discounts(purchase_value):
    if 200 < purchase_value:
        discount = 0.2
    elif 100 < purchase_value:
        discount = 0.1
    else:
        discount = 0.05

    total = purchase_value * (1 - discount)

    return print(f'O valor final é de R${total:.2f}. {int(discount * 100)}% OFF ')

#calculate_discounts(purchase_value)

# Exercício 4
#user = input('Usuário: ')
#password = input('Senha: ')

def verify_login(user, password):
    user_bd = 'admin'
    password_bd = '123456'

    isValidUser = user_bd == user and password_bd == password

    if not isValidUser:
        print('Usuário ou senha inválidos')
        return

    return print(f'Bem vindo {user}!')

#verify_login(user, password)