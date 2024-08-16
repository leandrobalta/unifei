def list_contains_elements_of_list(list1, list2):
  # Returns True if list1 contains all elements of list2, False otherwise.

  return all(element in list1 for element in list2)



b_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

a_list = [
    [5,6,7],
    [4,5,6,7,8,9],
    [10,11,12]
]

for a_item in a_list:
    for b_item in b_list:
        print(a_item, b_item)
        if list_contains_elements_of_list(a_item, b_item):
            print("Achou")
            #break
            
