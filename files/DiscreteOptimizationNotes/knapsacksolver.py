import time

def original_knapsack(n, K, values, weights):
    dp = [[0 for _ in range(K + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(K + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    result_value = dp[n][K]
    w = K
    included_items = [0] * n

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            included_items[i - 1] = 1
            w -= weights[i - 1]

    return result_value, included_items, 1

def knapsack_greedy_dp_hybrid(n, K, items):
    # Sort by value-to-weight ratio
    items.sort(key=lambda x: x[2], reverse=True)

    # Greedy approximation
    current_weight = 0
    current_value = 0
    included_items = [0] * n

    for value, weight, ratio, index in items:
        if current_weight + weight <= K:
            current_weight += weight
            current_value += value
            included_items[index] = 1

    # Dynamic programming for remaining capacity
    remaining_capacity = K - current_weight
    dp = [0] * (remaining_capacity + 1)

    for value, weight, _, index in items:
        if included_items[index] == 0:  # Exclude already included items
            for w in range(remaining_capacity, weight - 1, -1):
                dp[w] = max(dp[w], dp[w - weight] + value)

    result_value = current_value + dp[remaining_capacity]
    opt = 0  # Assuming the solution is not guaranteed to be optimal

    return result_value, included_items, opt

def solve_it(input_data):
    start_time = time.time()

    # Parse input
    lines = input_data.strip().split('\n')
    first_line = lines[0].split()
    n = int(first_line[0])
    K = int(first_line[1])

    values = []
    weights = []

    for i in range(1, n + 1):
        parts = lines[i].split()
        values.append(int(parts[0]))
        weights.append(int(parts[1]))

    try:
        if time.time() - start_time < 1:  # Set a timeout for the original method, e.g., 1 second
            result_value, included_items, opt = original_knapsack(n, K, values, weights)
            output_data = f"{result_value} {opt}\n" + " ".join(map(str, included_items))
            return output_data
    except:
        pass

    items = [(values[i], weights[i], values[i] / weights[i], i) for i in range(n)]
    result_value, included_items, opt = knapsack_greedy_dp_hybrid(n, K, items)
    output_data = f"{result_value} {opt}\n" + " ".join(map(str, included_items))
    return output_data
