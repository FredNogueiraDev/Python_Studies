def calcular_decimo_terceiro(salario_bruto, n_meses_trabalhados):
    salario_anual = (salario_bruto * n_meses_trabalhados) / 12

    inss = calculadora_inss(salario_anual)
    base_irpf = (salario_anual - inss)
    irpf = calculadora_irpf(base_irpf)
    descontos = (inss + irpf)

    primeira_parcela = (salario_anual / 2)
    segunda_parcela = (primeira_parcela - descontos)

    total = (primeira_parcela + segunda_parcela)

    return (f'Vr. primeira parcela: R${primeira_parcela:.2f}\n'
            f'Vr. segunda parcela: R${segunda_parcela:.2f}\n'
            f'Total: R${total:.2f}')

def calculadora_inss(base_inss):
    TETO_INSS = 908.85
    FAIXAS_INSS = [
        (1412.00, 0.075),
        (2666.68, 0.09),
        (4000.03, 0.12),
        (float('inf'), 0.14)
    ]

    inss = 0
    valor_restante = base_inss
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
        salario = float(input('Salário bruto: R$'))
        meses = int(input('N° meses trabalhados: '))

        resultado = calcular_decimo_terceiro(salario, meses)
        print(resultado)
    except ValueError as e:
        print(f"Erro: {e}")