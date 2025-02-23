def text():
    textpy = 'Pyth1abch2hon'
    newtext=textpy[:: -1]
    print('Task 1')
    print(textpy)
    print(newtext[3:9])
    print('------------')

    
def sort():
    print('Task 2')
    list =  [10, -7, 8, -100, -50, 32, 87, 117, -210]
    print(min(list))
    print(max(list))
    print(sorted(list))
    print('------------')
    
def sort_list():
    print('Task 3')
    numbers_str = input("Please enter Numbers: ")
    #'''Числа нужно вводить через запятую'''
    numbers = [int(x.strip()) for x in numbers_str.split(',')]
    print(numbers)
    new_numbers = numbers[:]
    if len(numbers) > 1:
        new_numbers[0], new_numbers[-1] = new_numbers[-1], new_numbers[0]
    print(new_numbers)
    print('------------')

