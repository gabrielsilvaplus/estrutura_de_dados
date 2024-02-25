while True:
    try:
        input_str = input('Digite dois números separados por um espaço: ')
        numbers = [float(num) for num in input_str.split()]

        if len(numbers) != 2:
            raise ValueError("Por favor, insira exatamente dois números.")

        number1 = numbers[0]
        number2 = numbers[1]

        lista_numbers = [number1, number2]
        print(f'Considerando os números {number1} e {number2}, o maior deles é: {max(lista_numbers)} ')
        break

    except ValueError as e:
        print(f"Erro: {e}. Por favor, insira dois números válidos.")
