# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and you
# may return the result in any order.

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        num_f1 = {}
        num_f2 = {}
        result = []

        # get the frequency of each number in nums1
        for num in nums1:
            num_f1[num] = num_f1.get(num, 0) + 1

        # get the frequency of each number in nums1
        for num in nums2:
            num_f2[num] = num_f2.get(num, 0) + 1

        for num in num_f1:
            if num in num_f2:
                count = min(num_f1[num], num_f2[num])
                result.extend([num] * count)

        return result
