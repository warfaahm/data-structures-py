# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longest_palindrome(self, s):
        n = len(s)
        aa = [[False] * n for _ in range(n)]
        start, end = 0, 0

        for i in range(n):
            aa[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j] and (length == 2 or aa[i + 1][j - 1]):
                    aa[i][j] = True

                    if length > end - start + 1:
                        start, end = i, j

        return s[start:end + 1]