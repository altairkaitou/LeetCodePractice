class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def checkCap(weights, days, capacity):
            total = 0
            count_day = 1

            for weight in weights:
                if total + weight > capacity:
                    count_day += 1
                    total = 0
                    if count_day > days:
                        return False
                total += weight  

            return True     

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            if checkCap(weights, days, mid):
                right = mid
            else:
                left = mid + 1
        return left


        