# Given an integer array nums, return true if any value appears at least
# twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n = set()
        for num in nums:
            if num in n:
                return True
            n.add(num)
        return False
