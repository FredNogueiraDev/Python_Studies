def fgts_simulator(balance: float, remaining_months: int, gross_salary: float) -> str:
    annual_tax_rate = 0.03
    fgts_contribution_rate = 0.08
    penalty_rate = 0.2
    fixed_amount = 650.00

    monthly_tax = annual_tax_rate / 12
    monthly_contribution = gross_salary * fgts_contribution_rate

    initial_amount = balance * (1 + monthly_tax) ** remaining_months

    if monthly_tax > 0:
        compound_factor = ((1 + monthly_tax) ** remaining_months - 1) / monthly_tax
    else:
        compound_factor = remaining_months
    amount_contributions = monthly_contribution * compound_factor

    total = (initial_amount + amount_contributions) * penalty_rate + fixed_amount

    return f'TOTAL: R${total:.2f} '

if __name__ == "__main__":
    try:
        balance = float(input('Qual o valor do saldo atual? R$'))
        gross_salary = float(input('Qual o valor do seu salário bruto? R$'))
        remaining_months = int(input('Quantos meses faltam para o saque? '))
        if balance < 0 or gross_salary < 0 or remaining_months < 0:
            raise ValueError("Valores não podem ser negativos")
        resultado = fgts_simulator(balance, remaining_months, gross_salary)
        print(resultado)
    except ValueError as e:
        print(f"Erro: {e}")