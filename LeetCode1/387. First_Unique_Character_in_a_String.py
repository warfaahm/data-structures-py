# Given a string s, find the first non-repeating character in it and return its index.
# If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:

        # create dictionary
        char_dict = {}
        for a in s:
            if a in char_dict:
                char_dict[a] += 1
            else:
                char_dict[a] = 1

        for i, a in enumerate(s):
            if char_dict[a] == 1:
                return i
        return -1
