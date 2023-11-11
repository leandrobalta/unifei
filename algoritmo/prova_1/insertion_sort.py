import random

def insertion_sort(unsorted_array):
    length = len(unsorted_array)
    for i in range(1, length):
        current_value = unsorted_array[i]
        j = i - 1
        while j >= 0 and unsorted_array[j] > current_value:
            unsorted_array[j+1] = unsorted_array[j]
            j = j-1
        unsorted_array[j+1] = current_value

    return unsorted_array



array = [random.randint(1, 100) for _ in range(100)]

sorted_array = insertion_sort(array)

print(sorted_array)

