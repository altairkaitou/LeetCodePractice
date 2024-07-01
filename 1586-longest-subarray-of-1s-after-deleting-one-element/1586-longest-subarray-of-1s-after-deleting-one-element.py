class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest_sub = 0
        start = 0
        count_zero = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                count_zero += 1
            
            if count_zero > 1:
                if nums[start] == 0:
                    count_zero -= 1
                start += 1
            
            longest_sub = max(longest_sub, end - start)
        
        if longest_sub == len(nums):
            return len(nums) - 1
        
        return longest_sub
        