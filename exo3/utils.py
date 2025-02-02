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
    print(f"object: {items}, max weight: {max_weight}")
    for i in range(1, n + 1):
        value, weight = items[i - 1]
        for w in range(max_weight + 1):
            if weight > w:
                tdp[i][w] = tdp[i - 1][w]  # don't take object because his weight > than the current maximal capicity of knapsack
            else:
                tdp[i][w] = max(tdp[i - 1][w], tdp[i - 1][w - weight] + value)

    # display tdp
    # print(tdp)

    # Retrieve the select objects
    w = max_weight
    selected_items = []
    for i in range(n, 0, -1):
        if tdp[i][w] != tdp[i - 1][w]:  # object have been taken
            selected_items.append(items[i - 1])
            w -= items[i - 1][1]

    return tdp[n][max_weight], selected_items