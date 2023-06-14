from week1.two_sum import twoSum

if __name__ == '__main__':
    assert twoSum(nums = [2,7,11,15], target = 9) == [0,1]
    assert twoSum(nums = [3,3], target = 6) == [0, 1]
    assert twoSum(nums = [3,2,4], target = 6) == [1, 2]
    print("Passed all the tests for two_sum 🎉")
