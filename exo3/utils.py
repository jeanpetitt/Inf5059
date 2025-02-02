def knapsack(items, max_weight):
    """
    Solve the problem of Knapsack 0/1 with Dynamic programing.
    :param items: tuples list (value, weight)
    :param max_weight: maximal capicity of Knapsack.
    :return: value maximal to fill and object selected.
    """
    n = len(items)
    tdp = [[0] * (max_weight + 1) for _ in range(n + 1)]

    # Filling of table of dp(tdp)
    for i in range(1, n + 1):
        value, weight = items[i - 1]
        for w in range(max_weight + 1):
            if weight > w:
                tdp[i][w] = tdp[i - 1][w]  # don't take object because his weight > than the current maximal capicity of knapsack
            else:
                tdp[i][w] = max(tdp[i - 1][w], tdp[i - 1][w - weight] + value)

    # display tdp
    print(tdp)

    # Retrieve the select objects
    w = max_weight
    selected_items = []
    for i in range(n, 0, -1):
        if tdp[i][w] != tdp[i - 1][w]:  # object have been taken
            selected_items.append(items[i - 1])
            w -= items[i - 1][1]

    return tdp[n][max_weight], selected_items


# list of object as form (value, wight)
items = [(60, 10), (100, 20), (120, 30)]

# maximale capacity of knapsack
max_weight = 50

max_value, selected_items = knapsack(items, max_weight)
print(f"maximum possible value : {max_value}")
print(f"Object selected : {selected_items}")