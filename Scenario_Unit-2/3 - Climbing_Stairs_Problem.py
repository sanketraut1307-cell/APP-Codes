def climbing_stairs(n):
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Accept input
n = int(input("Enter number of stairs: "))

# Calculate ways
ways = climbing_stairs(n)

print("Total number of ways:", ways)


# Input - 
# Enter number of stairs: 5
  
# Output - 
# Total number of ways: 8
