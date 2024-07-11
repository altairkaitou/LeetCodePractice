class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0

        freq = {}

        for num in nums:
            if num in freq:
                count += 1
                freq[num] += 1
            else:
                freq[num] = 1
        return count
        