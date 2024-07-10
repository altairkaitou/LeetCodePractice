class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        result = []
        all_sum = []
        sum = 0

        nums.sort()

        for i in range(len(nums)):
            sum += nums[i]
            all_sum.append(sum)
        
        def bns(all_sum, final):
            left = 0
            right = len(all_sum) - 1



            while left <= right:
                mid = left + (right - left) // 2

                if all_sum[mid] == final:
                    return mid
                elif all_sum[mid] < final:
                    left = mid + 1
                else:
                    right = mid - 1
            
            if all_sum[mid] > final:
                return mid - 1
            return mid 

        for q in queries:
            q_length = bns(all_sum, q)
            result.append(q_length + 1)


        
        

        return result

       
            




        