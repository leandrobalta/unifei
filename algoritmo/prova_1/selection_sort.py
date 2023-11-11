
import random

def selection_sort(unsorted): 
    length = len(unsorted)
    for i in range(length-1):
        min_index_available = i
        for j in range(i, length):
            if unsorted[j] < unsorted[min_index_available]:
                min_index_available = j

        unsorted[min_index_available], unsorted[i] = unsorted[i], unsorted[min_index_available]

    return unsorted

array = [random.randint(1, 100) for _ in range(100)]

sorted_array = selection_sort(array)

print(sorted_array)