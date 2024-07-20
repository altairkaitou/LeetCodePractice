class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        result = []
        nums.sort()

        for i in range(0, len(nums), 2):
            result.extend(nums[i:i + 2][::-1])
        
        return result
        