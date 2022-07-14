from main_code import calc_inss, calc_irpf

def teste_inss():

    """Testa se a função 'calc_inss' esta funcionando corretamente, abrangendo todas as suas variações de percentual """

    inss = calc_inss(1000)
    if inss == 80:
        print(f'Calculo INSS a 8% funcionando corretamente')
    else:
        print("Calculo incorreto")
    inss_2 = calc_inss(2000)
    if inss_2 == 180:
        print(f'Calculo INSS a 9% funcionando corretamente')
    else:
        print("Calculo incorreto")
    inss_3 = calc_inss(3000)
    if inss_3 == 330:
        print(f'Calculo INSS a 11% funcionando corretamente')
    else:
        print("Calculo incorreto")

def teste_irpf():
    """Testa se a função 'calc_irpf' esta funcionando corretamente, abrangendo todas as suas variações de percentual e dependentes""" 

    irpf = round(calc_irpf(1000, 330, 0),2)
    if irpf == 0:
        print(f'Calculo de imposto IRPF a 0% funcionando corretamente')
    else:
        print("Calculo incorreto")
    irpf = round(calc_irpf(2500, 225, 0),2)
    if irpf == 27.82:
        print(f'Calculo de imposto IRPF a 7,5% funcionando corretamente')
    else:
        print("Calculo incorreto")
    irpf = round(calc_irpf(3000, 330, 2),2)
    if irpf == 29.01:
        print(f'Calculo de imposto IRPF com dependente funcionando corretamente')
    else:
        print("Calculo incorreto")
    irpf = round(calc_irpf(3500, 385, 0),2)
    if irpf == 112.45:
        print(f'Calculo de imposto IRPF a 15% funcionando corretamente')
    else:
        print("Calculo incorreto")
    irpf = round(calc_irpf(4500, 495, 0),2)
    if irpf == 265:
        print(f'Calculo de imposto IRPF a 22,5% funcionando corretamente')
    else:
        print("Calculo incorreto")
    irpf = round(calc_irpf(6000, 642.34, 0),2)
    if irpf == 604:
        print(f'Calculo de imposto IRPF a 27,5% funcionando corretamente')
    else:
        print("Calculo incorreto")

if __name__ == "__main__":
    print('Testando INSS...')
    teste_inss()
    print('Testando IRPF...')
    teste_irpf()
    print('Testes Concluídos')