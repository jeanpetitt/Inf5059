
def binary_search(target, array):
    """
    Implement the binary search algorithm.
    
    :param array: sorted list
    :param target: value to find
    :return: index of the target value if found else -1
    """
    left, right = 0, len(array) - 1
    print(f"target: {target}, array: {array}")
    
    while left <= right:
        mid = (left + right) // 2  # find index of mid element
        
        if array[mid] == target:
            return mid  # target value == mid element
        elif array[mid] < target:
            left = mid + 1  # search target value after the mid element(right)
        else:
            right = mid - 1  # Search target value after the mid element(left)
            
    return -1  # Element not found


