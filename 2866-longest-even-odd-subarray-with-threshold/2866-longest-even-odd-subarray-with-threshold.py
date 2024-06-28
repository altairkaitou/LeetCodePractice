class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        answer = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                i += 1
                string_length = 1
                while (i < len(nums)):
                    if nums[i] % 2 == nums[i - 1] % 2 or nums[i] > threshold:
                        break
                    string_length += 1
                    i += 1
                
                i -= 1
                answer = max(answer, string_length)

        return answer
        