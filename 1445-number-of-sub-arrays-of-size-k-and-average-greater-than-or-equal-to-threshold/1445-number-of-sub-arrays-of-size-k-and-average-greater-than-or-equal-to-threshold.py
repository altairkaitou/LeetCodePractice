class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        i  = 0
        count = 0
        start = 0
        Countlen = 0

        for i in range(len(arr)):
            result += arr[i]
            Countlen += 1

            if Countlen == k:
                if result/k >= threshold:
                    count += 1
                    
                result -= arr[start]


                start += 1
                   
                Countlen -= 1

        return count
        

