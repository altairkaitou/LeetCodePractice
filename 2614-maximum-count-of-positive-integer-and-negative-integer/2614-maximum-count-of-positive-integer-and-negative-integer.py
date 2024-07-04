class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos_number = 0
        neg_number = 0

        for num in nums:
            if num > 0:
                pos_number += 1
            elif num < 0:
                neg_number += 1
        
        return pos_number if pos_number > neg_number else neg_number
        