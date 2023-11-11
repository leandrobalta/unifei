import random

def merge_sort(list):
    if len(list) == 1:
        return list
    
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    left_half = merge_sort(left)
    right_half = merge_sort(right)

    return merge(left_half, right_half)


def merge(left_half, right_half):
    top_left = top_right = 0
    merged_list = []

    while top_left < len(left_half) and top_right < len(right_half):
        if left_half[top_left] < right_half[top_right]:
            merged_list.append(left_half[top_left])
            top_left+=1
        else:
            merged_list.append(right_half[top_right])
            top_right+=1

    while top_left < len(left_half):
        merged_list.append(left_half[top_left])
        top_left+=1

    while top_right < len(right_half):
        merged_list.append(right_half[top_right])
        top_right+=1

    return merged_list


array = [random.randint(1, 100) for _ in range(100)]

sorted_array = merge_sort(array)

print(sorted_array)