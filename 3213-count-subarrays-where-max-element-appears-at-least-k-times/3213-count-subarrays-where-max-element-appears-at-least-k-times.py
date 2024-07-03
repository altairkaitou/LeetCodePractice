class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_number = max(nums)
        result = 0
        count = 0
        left = 0
        for num in nums:
            if num == max_number:
                count += 1
            while count == k:
                if nums[left] == max_number:
                    count -= 1
                left += 1
            result += left
        
        return result





        