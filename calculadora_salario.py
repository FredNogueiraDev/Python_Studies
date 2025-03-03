salario = float(input('Qual o valor do salário bruto? R$'))
horas_semanais = int(input('Quantas horas semanais? '))
he_dias_comuns = float(input('Quantas horas extras em dias comuns? '))
he_dias_feriados = float(input('Quantas horas extras em feriados/domingos? '))

def calcular_horas_extras(salario, horas_semanais, he_dias_comuns, he_dias_feriados):
    salario_hora = salario / (horas_semanais * 5)

    vr_horas_extras_comuns = salario_hora * he_dias_comuns * 1.75
    vr_horas_extras_feriados = salario_hora * he_dias_feriados * 2.0367

    vr_horas_extras_total = vr_horas_extras_comuns + vr_horas_extras_feriados

    return vr_horas_extras_total


def calcular_salario_liquido(salario, horas_semanais, he_dias_comuns, he_dias_feriados):
    vr_horas_extras = calcular_horas_extras(salario, horas_semanais, he_dias_comuns, he_dias_feriados)
    salario_total = salario + vr_horas_extras

    if salario_total <= 1412.00:
        inss = salario_total * 0.075
    elif salario_total <= 2666.68:
        inss = (1412.00 * 0.075) + ((salario_total - 1412.00) * 0.09)
    elif salario_total <= 4000.03:
        inss = (1412.00 * 0.075) + ((2666.68 - 1412.00) * 0.09) + ((salario_total - 2666.68) * 0.12)
    else:
        inss = (1412.00 * 0.075) + ((2666.68 - 1412.00) * 0.09) + ((4000.03 - 2666.68) * 0.12) + (
                    (salario_total - 4000.03) * 0.14)
        if inss > 908.85:
            inss = 908.85

    base_irpf = salario_total - inss

    if base_irpf <= 2259.20:
        irpf = 0
    elif base_irpf <= 2826.65:
        irpf = (base_irpf * 0.075) - 158.40
    elif base_irpf <= 3751.05:
        irpf = (base_irpf * 0.15) - 381.44
    elif base_irpf <= 4664.68:
        irpf = (base_irpf * 0.225) - 662.77
    else:
        irpf = (base_irpf * 0.275) - 896

    salario_liquido = salario_total - inss - irpf

    return (f'Salário bruto + horas extras: R${salario_total:.2f}\n'
            f'Horas extras: R${vr_horas_extras:.2f}\n'
            f'Desconto INSS: R${inss:.2f}\n'
            f'Desconto IRPF: R${irpf:.2f}\n'
            f'Salário líquido: R${salario_liquido:.2f}')


print(calcular_salario_liquido(salario, horas_semanais, he_dias_comuns, he_dias_feriados))

