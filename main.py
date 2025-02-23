import my_date
import my_sorted
import my_matrix
import my_sum

if __name__ == '__main__':
    my_sorted.text()
    my_sorted.sort()
    my_date.my_time()
    my_sorted.sort_list()
    print('Task 5')
    n = input(f'Please enter lines: ')
    m = input(f'Please enter column: ')
    my_matrix.printMatrix(n,m)
    my_sum