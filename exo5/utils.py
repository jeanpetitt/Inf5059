def max_subarray_sum(arr):
    """
    implement kadane algorithm to find the maximal sum of any contiguous subarray.
    :param arr: List of integers
    :return: maximal sum and corresponding subarray.
    """
    if not arr:
        return 0, []

    max_sum = float('-inf')
    current_sum = 0
    start = end = s = 0

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = s
            end = i

        if current_sum < 0:
            current_sum = 0
            s = i + 1

    return max_sum, arr[start:end+1]

# case 0
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, subarray = max_subarray_sum(arr)
print(f"case 1:\n max sum: {max_sum}, Corresponding subarray : {subarray}")

# case 2
max_sum, subarray = max_subarray_sum([1, 2, 3, 4, 5])
print(f"case 2: \n max sum: {max_sum}, Corresponding subarray : {subarray}")   

# case 3
max_sum, subarray = max_subarray_sum([-1, -2, -3, -4])
print(f"case 3: \n max sum: {max_sum}, Corresponding subarray : {subarray}")  

# case 3:
max_sum, subarray = max_subarray_sum([5, -1, -2, 10, -3, 2])

print(f"case 4: \n max sum: {max_sum}, Corresponding subarray : {subarray}")  
