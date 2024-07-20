class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        firstnumber = 0 
        secondnumber = 0

        for num in nums:
            if num > firstnumber:
                secondnumber = firstnumber
                firstnumber = num
            
            elif num > secondnumber:
                secondnumber = num
            
        
        return (firstnumber - 1) * (secondnumber - 1)

        