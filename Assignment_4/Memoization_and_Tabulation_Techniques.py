# Fibonacci using Dynamic Programming

# Memoization (Top-Down)
def fib_memo(num, cache):
    if num == 0 or num == 1:
        return num

    if cache[num] != -1:
        return cache[num]

    cache[num] = fib_memo(num - 1, cache) + fib_memo(num - 2, cache)
    return cache[num]


# Tabulation (Bottom-Up)
def fib_table(num):
    if num == 0:
        return 0
    if num == 1:
        return 1

    table = [0] * (num + 1)
    table[1] = 1

    for i in range(2, num + 1):
        table[i] = table[i - 1] + table[i - 2]

    return table[num]


# Driver Code
value = int(input("Enter Fibonacci position: "))

memory = [-1] * (value + 1)

answer1 = fib_memo(value, memory)
answer2 = fib_table(value)

print("\nResult using Memoization :", answer1)
print("Result using Tabulation  :", answer2)


#Output -
# Enter Fibonacci position: 12
# Result using Memoization : 144
# Result using Tabulation  : 144
