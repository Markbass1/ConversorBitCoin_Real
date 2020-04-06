bitcoin = 37763.316547
real = 0.000026

# apresentacao
while True:
    print("\n \n Bem vindo ao Conversor de Criptomoedas")
    print(" 1 - Converter Bitcoins em Reais \n 2 - Converter Reais em Bitcoins \n 3 - Sair")
    menu = input("Digite um nomero para prosseguir:")
    if menu == "1":
        print("Bitcoins para Reais")
        valor_bit = float(input("digite o valor em bitcoins para conversao: "))
        print("R$ " + str(round(valor_bit*bitcoin, 2)))
    elif menu == "2":
        print("Reais para Bitcoins")
        valor_real = float(input("digite o valor em Reais para conversao: "))
        print("Bit$: " + str(round(valor_real*real, 2)))
    elif menu == "3":
        controle = 0
        print("Obrigado por utilizar nosso conversor. Ate a proxima")
        break
    else:
        print("Menu solicitado inexistente. Por favor tente novamente")
