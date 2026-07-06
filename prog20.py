cargo = input('Digite o seu cargo na empresa (caixa, vendedor ou gerente): ')
if cargo == 'caixa':
    salário = 1500
    print(salário)
    inss = (salário*12)/100
    print(inss)
    irrf = (salário*8)/100
    print(irrf)
    salárioFinal = salário - inss - irrf
    print(salárioFinal)
elif cargo == 'vendedor':
    salário = 2400
    print(salário)
    inss = (salário*12)/100
    print(inss)
    irrf = (salário*14)/100
    print(irrf)
    salárioFinal = salário - inss - irrf
    print(salárioFinal)
elif cargo == 'gerente':
    salário = 4000
    print(salário)
    inss = (salário*12)/100
    print(inss)
    irrf = (salário*14)/100
    print(irrf)
    salárioFinal = salário - inss - irrf
    print(salárioFinal)
elif cargo != 'caixa' and 'vendedor' and 'gerente':
    print('Cargo invalido! Digite um cargo valido.')