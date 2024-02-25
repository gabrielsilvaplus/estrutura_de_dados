while True:
    try:
        nota = float(input("Digite uma nota entre zero e dez: "))
        
        if 0 <= nota <= 10:
            print(f"Nota válida: {nota}")
            break
        else:
            print("Nota inválida. Por favor, digite um valor entre zero e dez.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
