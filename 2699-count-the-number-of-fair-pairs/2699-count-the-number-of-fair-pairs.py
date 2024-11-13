class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.counting(nums, upper) - self.counting(nums, lower - 1)

    
    def counting(self, nums, target):
        i, j = 0, len(nums) - 1
        res = 0
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                res += j - i
                i += 1
        
        return res







        
        