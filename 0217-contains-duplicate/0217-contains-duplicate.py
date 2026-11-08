class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        """ store somehow using a set? we need to keep track of the nums
        then count if there are dups """
        """ if it's already in the set, you found a dup, otherwise add it """
        seen = set() # initialize
        for num in nums:
            if num in seen:
                return True
            seen.add(num) # keep track
        return False



