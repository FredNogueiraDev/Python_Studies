def remuneracao_liq_efetiva(salario_bruto, vale_refeicao, vale_transporte, outros_beneficios):
    inss_base = calculadora_inss(salario_bruto)
    irpf_base = calculadora_irpf(salario_bruto - inss_base)

    vr_ferias = calculadora_ferias(salario_bruto, 30)
    inss_ferias = calculadora_inss(vr_ferias)
    irpf_ferias = calculadora_irpf(vr_ferias - inss_ferias)
    vr_ferias_mensal = vr_ferias / 12

    decimo_terceiro = calcular_decimo_terceiro(salario_bruto, 12)
    inss_decimo = calculadora_inss(decimo_terceiro)
    irpf_decimo = calculadora_irpf(decimo_terceiro - inss_decimo)
    decimo_mensal = decimo_terceiro / 12

    fgts = calcula_fgts(salario_bruto)
    desc_vale_transporte = min(salario_bruto * 0.06, vale_transporte)

    receitas = (salario_bruto + vr_ferias_mensal + decimo_mensal +
                fgts + outros_beneficios + vale_transporte + vale_refeicao)
    inss_total = inss_base + ((inss_ferias + inss_decimo) / 12)
    irpf_total = irpf_base + ((irpf_ferias + irpf_decimo) / 12)

    despesas = desc_vale_transporte + inss_total + irpf_total
    salario_liquido = receitas - despesas

    demonstrativo = (
        '---------------------------------------\n'
        f'(+) Salário Bruto Mensal: R${salario_bruto:.2f}\n'
        f'(+) Vale Transporte: R${vale_transporte:.2f}\n'
        f'(+) Vale Refeição: R${vale_refeicao:.2f}\n'
        f'(+) Outros Benefícios: R${outros_beneficios:.2f}\n'
        f'(+) Parcela Férias: R${vr_ferias_mensal:.2f}\n'
        f'(+) Parcela 13º Salário: R${decimo_mensal:.2f}\n'
        f'(+) FGTS Mensal: R${fgts:.2f}\n'
        f'(-) INSS Total: R${inss_total:.2f}\n'
        f'(-) IRPF Total: R${irpf_total:.2f}\n'
        f'(-) Desconto Vale Transporte: R${desc_vale_transporte:.2f}\n'
        '---------------------------------------\n'
        f'(=) Salário Líquido Efetivo: R${salario_liquido:.2f}'
    )

    return demonstrativo

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

def calcular_decimo_terceiro(salario_bruto, n_meses_trabalhados):
    salario_anual = (salario_bruto * n_meses_trabalhados) / 12

    inss = calculadora_inss(salario_anual)
    base_irpf = (salario_anual - inss)
    irpf = calculadora_irpf(base_irpf)
    descontos = (inss + irpf) * 0

    primeira_parcela = (salario_anual / 2)
    segunda_parcela = (primeira_parcela - descontos)

    total = (primeira_parcela + segunda_parcela)

    return total

def calcula_fgts(salario_bruto):
    total = salario_bruto * 0.08
    return total

def calculadora_ferias(salario_bruto, dias_ferias):
    valor_diario = salario_bruto / 30
    ferias_base = valor_diario * dias_ferias
    adicional_um_terco = ferias_base / 3
    total_ferias_bruto = ferias_base + adicional_um_terco

    inss = calculadora_inss(total_ferias_bruto)

    base_irpf = total_ferias_bruto - inss
    irpf = calculadora_irpf(base_irpf)

    descontos = (inss + irpf) * 0
    total_liquido = total_ferias_bruto - descontos

    return total_liquido

if __name__ == "__main__":
    try:
        salario = float(input('SALÁRIO BRUTO: R$'))
        vale_refeicao = float(input('VALOR VALE REFEIÇÃO: '))
        vale_transporte = float(input('VALOR VALE TRANSPORTE: '))
        outros_beneficios = float(input('VALOR OUTROS BENEFICIOS (Vr. Líquido Mensal): '))

        resultado = remuneracao_liq_efetiva(salario, vale_refeicao, vale_transporte, outros_beneficios)
        print(resultado)
    except ValueError as e:
        print(f"Erro: {e}")