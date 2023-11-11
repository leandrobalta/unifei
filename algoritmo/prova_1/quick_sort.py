import random

def quick_sort(unsorted, start=0, end=None):
    if end == None:
        end = len(unsorted)-1
        print(end)
    if start < end:
        p = partition(unsorted, start, end)
        quick_sort(unsorted, start, p-1)
        quick_sort(unsorted, p+1, end)
    return unsorted

def partition(array, start, end):
    pivot = array[end]
    i = start
    for j in range(start, end):
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i = i+1
    array[i], array[end] = array[end], array[i]
    return i 

array = [random.randint(1, 100) for _ in range(100)]

sorted_array = quick_sort(array)

print(sorted_array)