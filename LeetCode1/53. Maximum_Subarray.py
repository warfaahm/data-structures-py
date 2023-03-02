# Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]  # maximum sum
        curr = 0  # current sum

        for num in nums:
            curr += num
            if max_sum < curr:
                max_sum = curr
            if curr < 0:
                curr = 0
        return max_sum
