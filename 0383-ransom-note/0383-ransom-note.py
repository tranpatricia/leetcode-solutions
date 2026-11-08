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

The tradeoff is complexity:
Each .count() scans the whole string, so every unique letter costs one full pass over the note and one over the magazine.
Time: O(u × (n + m)), where u is the number of unique letters in the note.
For this problem, that’s effectively O(n + m), because LeetCode says the input is lowercase English letters, so u is at most 26, a constant.
For general input, like any Unicode characters, u could grow with the input, approaching O(n × m) in the worst case. The dictionary version stays O(n + m) no matter the alphabet.
"""
