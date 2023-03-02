# Given a string s, find the length of the longest substring
# without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str)-> int:
        curr = set()
        len_max = 0
        x = 0

        for l, char in enumerate(s):
            while char in curr:
                curr.remove(s[x])
                x += 1
            curr.add(char)
            len_max = max(len_max, l - x + 1)
        return len_max