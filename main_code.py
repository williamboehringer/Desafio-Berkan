def calc_inss(salario: float) -> float:
    '''  Recebe parâmetro 'salario'(float) e retorna imposto INSS(float) '''

    if salario <= 1751.81:
        inss = salario * 0.08
    elif salario <= 2912.72:
        inss = salario * 0.09
    elif salario <= 5839.45:
        inss = salario * 0.11
    else:
        inss = 642.34

    return inss

def calc_irpf(salario: float, inss: float, dependentes: int) -> float:
    ''' 
    Recebe os parâmetros:
    salario(float)
    inss(float)
    dependentes(int)

    Retorna:
    irpf(float)
    '''
    
    val_depen = dependentes * 189.59
    salario_inss =  salario - inss - val_depen

    if salario_inss <= 1903.98:
        irpf = 0.00
    elif salario_inss <= 2826.65:
        irpf = salario_inss * 0.075
        irpf -= 142.80
    elif salario_inss <= 3751.05:
        irpf = salario_inss * 0.15
        irpf -= 354.80
    elif salario_inss <= 4664.68:
        irpf = salario_inss * 0.225
        irpf -= 636.13
    elif salario_inss > 4664.68:
        irpf = salario_inss * 0.275
        irpf -= 869.36

    return irpf

def calc_init():
    print()
    print('------------------------------------------------------------------')
    print('-           Bem-Vindo ao Sistema de Cálculo de Imposto           -')
    print('------------------------------------------------------------------')
    print()

    while True:
        try:
            salario = input('Digite seu salário: ')
            salario = float(salario.replace(",", "."))
            dependentes = int(input('Insira o número de dependentes: '))
            inss = calc_inss(salario)
            irpf = calc_irpf(salario, inss, dependentes)
            imposto_total = irpf + inss
            salario_final = salario - imposto_total

            print(f'Imposto INSS: R$ {inss:.2f}')
            print(f'Imposto IRPF: R$ {irpf:.2f}')
            print(f'Imposto Total: R$ {imposto_total:.2f}')
            print(f'Salario final: R$ {salario_final:.2f}\n')

            calc_novamente = input('Deseja calcular novamente? [s] sim - [n] não ')
            if calc_novamente == 's':
                continue
            elif calc_novamente == 'n':
                print('Programa Encerrado')
                return
            else:
                print('Comando invalido, digite novamente')
                break

        except ValueError:
            print('Número inválido. Tente novamente')

if __name__ == "__main__":
    calc_init()