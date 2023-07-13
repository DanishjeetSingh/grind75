def climbStairs(n):
    # no need to assign more spaces than needed, the question constraint mentions 45 btw
    # n+1 because of 0th index
    steps = [0] * (n + 1)
    steps[0] = steps[1] = 1

    # remember python range end is not inclusive
    for i in range(2, n + 1):
        steps[i] = steps[i - 1] + steps[i - 2]

    return steps[n]