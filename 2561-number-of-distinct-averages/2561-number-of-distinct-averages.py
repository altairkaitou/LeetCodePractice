class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        a = []

        for i in range(0, len(nums)//2):
            a.append((max(nums) + min(nums))/ 2)
            nums.remove(max(nums))
            nums.remove(min(nums))
            b = set(a)
    
        return len(b)
        