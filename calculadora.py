
def exibir_opc():
    print("\n=======OPERAÇÃO=======")
    print(" + ")
    print(" - ")
    print(" x ")
    print(" / ")
    print(" Sair ")

while True:
    exibir_opc()
    opc = input("Informe a operação: ").lower()

    match opc:
        case "+":
            n = float(input("Informe o primeiro número: "))
            n1 = float(input("Informe o segundo número: "))
            print(f"Seu resultado é {n+n1}")

        case "-":
            n = float(input("Informe o primeiro número: "))
            n1 = float(input("Informe o segundo número: "))
            print(f"Seu resultado é {n-n1}")

        case "x":
            n = float(input("Informe o primeiro número: "))
            n1 = float(input("Informe o segundo número: "))
            print(f"Seu resultado é {n*n1}")

        case "/":
            n = float(input("Informe o primeiro número: "))
            n1 = float(input("Informe o segundo número: "))
            while n1 == 0:
                print("Não é possível dividir por zero! Tente novamente.")
                n1 = float(input("Informe o segundo número: "))
            print(f"Seu resultado é {n/n1}")
        
        case "sair":
            print("Saindo...")
            break
        
        case _:
            print("Opção inválida!")
        