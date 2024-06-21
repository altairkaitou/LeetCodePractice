class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in hash_map:
                return [hash_map[complement], index]
            hash_map[value] = index 

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        