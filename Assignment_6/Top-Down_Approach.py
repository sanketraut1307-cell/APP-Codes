def knapsack_top_down(weights, values, capacity):
    n = len(weights)

    # Memoization table
    memo = [[-1 for _ in range(capacity + 1)]
            for _ in range(n + 1)]

    def solve(i, w):

        # Base condition
        if i == 0 or w == 0:
            return 0

        # Already calculated
        if memo[i][w] != -1:
            return memo[i][w]

        # If item cannot fit
        if weights[i - 1] > w:
            memo[i][w] = solve(i - 1, w)

        else:
            # Include the item
            include = values[i - 1] + solve(
                i - 1,
                w - weights[i - 1]
            )

            # Exclude the item
            exclude = solve(i - 1, w)

            memo[i][w] = max(include, exclude)

        return memo[i][w]

    return solve(n, capacity)


# Main program
weights = [2, 1, 3, 2]
values = [12, 10, 20, 15]
capacity = 5

result = knapsack_top_down(weights, values, capacity)

print("Maximum Value:", result)

# Output - 
# Maximum Value: 37
