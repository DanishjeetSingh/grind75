# https://leetcode.com/problems/two-sum/

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    required = {}
    for i in range (len(nums)):
        if target - nums[i] in required:
            return [required[target - nums[i]],i]
        else:
            required[nums[i]] = i