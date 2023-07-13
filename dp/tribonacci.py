def tribonacci(n)
    # here we can't do n*1 since 0 is included as a acceptable input, which can cause issues in line 5
    steps = [0] * 38
    steps[0] = 0
    steps[1], steps[2] = 1, 1

    for i in range(3, n + 1):
        steps[i] = steps[i - 1] + steps[i - 2] + steps[i - 3]

    return steps[n]