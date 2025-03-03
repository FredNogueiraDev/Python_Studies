
def calcular_horas_extras(salario, horas_semanais, he_dias_comuns, he_dias_feriados):
    qtd_dias_semana = 5
    porcentagem_hora_extra = 1.5
    porcentagem_hora_extra_dobro = 2

    salario_hora = salario / (horas_semanais * qtd_dias_semana)

    vr_horas_extras_comuns = salario_hora * he_dias_comuns * porcentagem_hora_extra
    vr_horas_extras_feriados = salario_hora * he_dias_feriados * porcentagem_hora_extra_dobro

    vr_horas_extras_total = vr_horas_extras_comuns + vr_horas_extras_feriados

    return vr_horas_extras_total

def calcular_salario_liquido(salario, horas_semanais, he_dias_comuns, he_dias_feriados):
    vr_horas_extras = calcular_horas_extras(salario, horas_semanais, he_dias_comuns, he_dias_feriados)
    salario_total = salario + vr_horas_extras

    inss = calculadora_inss(salario_total)
    base_irpf = salario_total - inss
    irpf = calculadora_irpf(base_irpf)

    salario_liquido = salario_total - inss - irpf

    return (f'Salário bruto + horas extras: R${salario_total:.2f}\n'
            f'Horas extras: R${vr_horas_extras:.2f}\n'
            f'INSS: R${inss:.2f}\n'
            f'IRPF: R${irpf:.2f}\n'
            f'Salário líquido: R${salario_liquido:.2f}')

def calculadora_inss(total_ferias_bruto):
    TETO_INSS = 908.85
    FAIXAS_INSS = [
        (1412.00, 0.075),
        (2666.68, 0.09),
        (4000.03, 0.12),
        (float('inf'), 0.14)
    ]

    inss = 0
    valor_restante = total_ferias_bruto
    for limite, aliquota in FAIXAS_INSS:
        if valor_restante <= 0:
            break
        faixa_anterior = FAIXAS_INSS[FAIXAS_INSS.index((limite, aliquota)) - 1][0] if FAIXAS_INSS.index((limite, aliquota)) > 0 else 0
        base_calculo = min(valor_restante, limite - faixa_anterior)
        inss += base_calculo * aliquota
        valor_restante -= base_calculo
    inss = min(inss, TETO_INSS)

    return inss

def calculadora_irpf(base_irpf):
    FAIXAS_IRPF = [
        (2259.20, 0, 0),
        (2826.65, 0.075, 158.40),
        (3751.05, 0.15, 381.44),
        (4664.68, 0.225, 662.77),
        (float('inf'), 0.275, 896)
    ]

    irpf = 0
    for limite, aliquota, deducao in FAIXAS_IRPF:
        if base_irpf <= limite:
            irpf = (base_irpf * aliquota) - deducao
            break

    return irpf

if __name__ == "__main__":
    try:
        salario = float(input('SALÁRIO BRUTO: R$'))
        horas_semanais = int(input('HORAS DE TRABALHO SEMANAIS: '))
        he_dias_comuns = float(input('HORAS EXTRAS EM DIAS COMUNS: '))
        he_dias_feriados = float(input('HORAS EXTRAS EM DOMINGOS/FERIADOS: '))

        resultado = calcular_salario_liquido(salario, horas_semanais, he_dias_comuns, he_dias_feriados)
        print(resultado)
    except ValueError as e:
        print(f"Erro: {e}")