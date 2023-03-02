# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

class Solution:
        def twoSum(self, nums: list[int], target: int) -> list[int]:
            for x, a in enumerate(nums):
                for y, b in enumerate(nums[x+1:], x+1):
                    if (a + b) == target:
                        return [x, y]
