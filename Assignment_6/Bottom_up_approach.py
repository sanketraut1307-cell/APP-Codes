def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                # Include or exclude the item
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                # Cannot include the item
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Main program
weights = [2, 1, 3, 2]
values = [12, 10, 20, 15]
capacity = 5

result = knapsack_bottom_up(weights, values, capacity)

print("Maximum Value:", result)


# Output - 
# Maximum Value: 37
