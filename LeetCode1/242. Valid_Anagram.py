# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}

        if len(s) != len(t):
            return False

        for a in s:
            if a in s_dict:
                s_dict[a] += 1
            else:
                s_dict[a] = 1
        for b in t:
            if b in s_dict and s_dict[b] > 0:
                s_dict[b] -= 1
            else:
                return False
        return True
