# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.

#
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        min_i, max_i, len_half = 0, m, (m + n + 1) // 2
        while min_i <= max_i:
            i = (min_i + max_i) // 2
            j = len_half - i
            if i < m and nums2[j-1] > nums1[i]:
                min_i = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                max_i = i - 1
            else:
                if i == 0: max_left = nums2[j-1]
                elif j == 0: max_left = nums1[i-1]
                else: max_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_left

                if i == m: min_right = nums2[j]
                elif j == n: min_right = nums1[i]
                else: min_right = min(nums1[i], nums2[j])

                return (max_left + min_right) / 2.0
