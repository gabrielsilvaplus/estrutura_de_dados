my_list = []


def calculate_average(list):
    if not list:
        return None
    else:
        total = sum(list)
        media = total / len(list)
        return media


for x in range(1, 6):
    n = float(input(f'Digite o valor {x}:  '))
    my_list.append(n)

result = calculate_average(my_list)
if my_list is not None:
    print(f'A média é: {result:.2f}')
else:
    print('A lista está vazia!')
