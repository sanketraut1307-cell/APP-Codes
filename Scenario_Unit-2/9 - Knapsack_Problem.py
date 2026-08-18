def knapsack(weights, values, capacity):
    n = len(weights)

    # DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Accept input
weights = list(map(int, input("Enter item weights: ").split()))
values = list(map(int, input("Enter item values: ").split()))
capacity = int(input("Enter bag capacity: "))

# Calculate maximum value
max_value = knapsack(weights, values, capacity)

print("Maximum obtainable value:", max_value)

# Output - 
# Enter item weights: 2 3 4 5
# Enter item values: 3 4 5 6
# Enter bag capacity: 5
