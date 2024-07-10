class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        prefix_sum = []
        result = 0

        nums.sort()
        total = []

        for num in nums:
            result += num
            prefix_sum.append(result)
        
        def binarysearch(prefix_sum, q):
            left = 0
            right = len(prefix_sum) - 1
            while (left <= right):
                mid = left + (right - left) // 2
                if prefix_sum[mid] == q:
                    return mid
                elif prefix_sum[mid] > q:
                    right = mid - 1
                else:
                    left = mid + 1
            if prefix_sum[mid] > q:
                return mid - 1
            
            return mid 
            
        for q in queries:
            final = binarysearch(prefix_sum, q)
            total.append(final + 1)
        return total 
                    
        

            
        