# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                for j in range(len(matrix[i])):
                    if target == matrix[i][j]:
                        return True
        return False
