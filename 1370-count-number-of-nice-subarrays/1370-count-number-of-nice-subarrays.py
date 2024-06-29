class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        start = 0
        result = 0
        count = 0
        for end in range(len(nums)):
            if nums[end] % 2 != 0:
                k -= 1
                count = 0
            while k == 0:
                count += 1
                k += (nums[start] % 2)
                start += 1
            result += count
        return result
        