class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        sum = 0 

        map_sum = defaultdict(int)
        map_sum[0] = 1
        count = 0

        for num in nums:
            sum += num

            if sum - goal in map_sum:
                count += map_sum[sum - goal]
            
            map_sum[sum] = map_sum[sum] + 1
        
        return count

        