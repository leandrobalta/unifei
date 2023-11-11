

def bubble_sort(array):
    lenght = len(array)

    for i in range(lenght-1):
        for j in range(lenght-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    
    return array
        
    
array = [2,4,51,5,36,3,1,5,6,7,8]

print(f"sorted list: {bubble_sort(array)}")