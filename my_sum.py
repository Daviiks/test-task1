def sum_1(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer.")
    total = 0
    for i in range(1, n + 1):
        total += (1 / i)**2
    return total

def sum_2(m, n):
    if not isinstance(m, int) or m <= 0 or not isinstance(n, int) or n <= 0:
        raise ValueError("m and n must be positive integers.")
    total = 0
    for i in range(1, m + 1):
        total += i**n
    return total

def select_operation(operation):
    if operation == 1:
        return sum_1
    elif operation == 2:
        return sum_2
    else:
        raise ValueError('Invalid operation value. Valid values: 1 or 2.')

# Главный блок программы
while True: # Цикл для повторного ввода, если введены некорректные данные
    try:
        print('Task 4')
        operation = int(input("Select operation (1 or 2):\n"
                              "1: Calculate Sum 1 + (1/2)^2 + (1/3)^2 + ... + (1/n)^2\n"
                              "2: Calculate Sum 1^n + 2^n + 3^n + ... + m^n\n"
                              "Enter transaction number: "))
        selected_operation = select_operation(operation)

        if operation == 1:
            n = int(input('Enter value n: '))
            result = selected_operation(n)
            print(f'Result of the operation 1 (n = {n}): {result}')
            print('------------')
            break # Выход из цикла при успешном выполнении
        elif operation == 2:
            m = int(input('Enter value m: '))
            n = int(input('Enter value n: '))
            result = selected_operation(m, n)
            print(f'Result of the operation 2 (m = {m}, n = {n}): {result}')
            print('------------')
            break # Выход из цикла при успешном выполнении
    except ValueError as e:
        print(f'Error: {e}. Please try again.')
