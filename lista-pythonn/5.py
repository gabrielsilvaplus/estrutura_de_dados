number = input('Digite um número: ')

try:
    number_f = float(number)
except ValueError:
    print(f'O que você digitou({number}) não é um número.')
    exit()

if number_f == 0:
    print(f'O número {number} é neutro.')
elif number_f > 0:
    print(f'O número {number} é positivo.')
elif number_f < 0:
    print(f'O número {number} é negativo.')
