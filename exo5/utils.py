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
    print(f'Array: {arr}')

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
