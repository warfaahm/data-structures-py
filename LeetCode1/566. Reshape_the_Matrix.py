# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix
# into a new one with a different size r x c keeping its original data.
# You are given an m x n matrix mat and two integers r and c representing the number of rows
# and the number of columns of the wanted reshaped matrix.
# The reshaped matrix should be filled with all the elements of the original matrix in the same
# row-traversing order as they were.

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        flat = []
        new_res = []

        for rr in mat:
            for num in rr:
                flat.append(num)

        if r * c != len(flat):
            return mat
        else:
            for i in range(r):
                new_res.append(flat[i * c: i * c + c])
            return new_res
