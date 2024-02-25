numbers_list = []


def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Insira um número corretamente.")


for x in range(1, 4):
    num = get_number("Digite o primeiro número: ")
    numbers_list.append(num)

numbers_list.sort(reverse=True)

print(f'Os números em ordem decrescente são: {numbers_list[0]}, {numbers_list[1]}, {numbers_list[2]}')
