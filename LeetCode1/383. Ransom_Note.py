# Given two strings ransomNote and magazine, return true if ransomNote can be
# constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = {}

        for a in magazine:
            if a in mag_dict:
                mag_dict[a] += 1
            else:
                mag_dict[a] = 1

        for x in ransomNote:
            if x in mag_dict and mag_dict[x] > 0 :
                mag_dict[x] -= 1
            else:
                return False
        return True
