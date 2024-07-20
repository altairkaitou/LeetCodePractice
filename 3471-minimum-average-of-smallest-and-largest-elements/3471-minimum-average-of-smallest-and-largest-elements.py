class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg = []
        minNum = float('inf')
        for i in range(len(nums) // 2):
            minN = min(nums)
            maxN = max(nums)

            avg.append((minN + maxN) / 2)

            nums.remove(minN)
            nums.remove(maxN)
        
        return min(avg)



        