def binary_search(item_list, value_to_find):
    left_end = 0
    right_end = len(item_list)
    while left_end <= right_end:
        middle_index = left_end + (right_end - left_end) // 2
        item = item_list[middle_index]
        if item == value_to_find:
            return middle_index
        elif item < value_to_find:
            left_end = middle_index + 1
        else:
            right_end = middle_index - 1
    return None


array = ["1", "and", "beta", "can", "door", "e", "zoom"]
x = "1"

index = binary_search(array, x)
if index is not None:
    print("Item is at index: " + str(index) +
          "\nIt is element " + str(index + 1) + " in the list.")
else:
    print("Item not found.")
