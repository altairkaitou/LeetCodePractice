"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        result = []


        def bns(x, target):
            left = 1
            right = 1000

            while left <= right:
                y = left + (right - left) // 2
                result = customfunction.f(x, y)
                if result == target:
                    return y
                elif result > target:
                    right = y - 1
                else:
                    left = y + 1
            
            return None 

        for x in range(1, 1001):
            y = bns(x, z)
            if y:
                result.append([x,y])
        
        return result

        