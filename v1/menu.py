def menu(lista):
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    opc = int(input('Sua opção :'))
    return opc