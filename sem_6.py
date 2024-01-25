# Задача. Написать программу на любом языке в любой парадигме для бинарного поиска. 
# На вход подаётся целочисленный массив и число. На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.

def binary_search(arr, element):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_element = arr[middle]

        if element == middle_element:
            return middle
        elif element < middle_element:
            right = middle - 1
        else:
            left = middle + 1

    return -1

def main():
    index = binary_search([1, 3, 5, 7, 9], 5)
    print(index)
    index2 = binary_search([1, 3, 5, 7, 9], 8)
    print(index2)

if __name__ == "__main__":
    main()