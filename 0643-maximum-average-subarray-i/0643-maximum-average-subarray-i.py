class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = 0

        for i in range(k):
            current_sum += nums[i]
        
        max_value = current_sum

        left = 0
        right = k
        while right < len(nums):
            current_sum -= nums[left]
            left += 1
            current_sum += nums[right]
            right += 1
            max_value = max(max_value, current_sum)
        
        return max_value/k
        