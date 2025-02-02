
def binary_search(target, array):
    """
    Implement the binary search algorithm.
    
    :param array: sorted list
    :param target: value to find
    :return: index of the target value if found else -1
    """
    left, right = 0, len(array) - 1
    
    while left <= right:
        mid = (left + right) // 2  # find index of mid element
        
        if array[mid] == target:
            return mid  # target value == mid element
        elif array[mid] < target:
            left = mid + 1  # search target value after the mid element(right)
        else:
            right = mid - 1  # Search target value after the mid element(left)
            
    return -1  # Element not found

# Example of sorted lists  and targets to find
sorted_lists = [
    ([1, 3, 5, 7, 9, 11, 13], 7),    # Target in the list
    ([2, 4, 6, 8, 10, 12], 5),       # absent in the list 
    ([0, 1, 2, 3, 4, 5, 6], 0),      # First element
    ([10, 20, 30, 40, 50], 50),      # last element
]

for arr, target in sorted_lists:
    result = binary_search(target, arr)
    print(f"Search of {target} in {arr} → Index: {result}")


