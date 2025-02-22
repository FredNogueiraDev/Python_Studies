balance = float(input('Qual o valor do saldo atual? R$'))
monthly_contribution = float(input('Qual o valor do aporte mensal em média? R$'))
remaining_months = int(input('Quantos meses faltam para o saque? '))

def fgts_simulator(balance, remaining_months, monthly_contribution):
    tax = 0.03 / 12

    initial_amount = balance * (1 + tax) ** remaining_months
    amount_contributions = monthly_contribution * (( (1 + tax) ** remaining_months - 1 ) / tax)
    total =  (((initial_amount + amount_contributions) * 0.2) + 650)

    result = f'O seu saque aniversário ficará em torno de R${total:.2f} '

    return result

print(fgts_simulator(balance, remaining_months, monthly_contribution))
