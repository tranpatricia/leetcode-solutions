class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counts = {}

        for letter in magazine:
            counts[letter] = counts.get(letter, 0) + 1

        for letter in ransomNote:
            if counts.get(letter, 0) == 0:
                return False
            counts[letter] -= 1
        return True

"""
adding this sample solution using a set in 3ms runtime:
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for char in set(ransomNote):
            if ransomNote.count(char) > magazine.count(char):
                return False
        return True
"""
