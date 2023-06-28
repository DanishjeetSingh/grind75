from week1.two_sum import two_sum

if __name__ == '__main__':
    assert two_sum(nums = [2,7,11,15], target = 9) == [0,1]
    assert two_sum(nums = [3,3], target = 6) == [0, 1]
    assert two_sum(nums = [3,2,4], target = 6) == [1, 2]
    print("Passed all the tests for two_sum 🎉")
