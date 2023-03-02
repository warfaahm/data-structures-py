# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        new_list = []

        for x in range(numRows):
            row = [1] * (x + 1)
            for y in range(1, x):
                row[y] = new_list[x-1][y-1] + new_list[x-1][y]
            new_list.append(row)
        return new_list
