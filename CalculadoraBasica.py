while True:
    print("0 : Soma")
    print("1 : Subtração")
    print("2 : Multiplicação ")
    print("3 : Divisão ")
    print("4 : Exponenciação")

    escolha = int(input("Escolha a operação que deseja realizar: "))

    if escolha == 0:
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        n3 = n1 + n2
        print("A soma foi:", n3)
        n1 = 0
        n2 = 0
        n3 = 0

    elif escolha == 1:
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        n3 = n1 - n2
        print("A subtração foi:", n3)
        n1 = 0
        n2 = 0
        n3 = 0

    elif escolha == 2:
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        n3 = n1 * n2
        print("A multiplicação foi:", n3)
        n1 = 0
        n2 = 0
        n3 = 0

    elif escolha == 3:
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        n3 = n1 / n2
        print("A divisão foi:", n3)
        n1 = 0
        n2 = 0
        n3 = 0

    elif escolha == 4:
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        n3 = n1 ** n2
        print("A exponenciação foi:", n3)
        n1 = 0
        n2 = 0
        n3 = 0

    else:
        print("Operação inválida. Tente novamente.")
        continue

    opcao_continuar = input("Deseja continuar? (s/n):")

    if opcao_continuar.lower() == 's':
        n1 = 0
        n2 = 0
        n3 = 0
        continue

    else:
        print("Encerrando o programa.")
        break
