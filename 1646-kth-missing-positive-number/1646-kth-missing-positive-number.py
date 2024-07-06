class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        current_num = 1

        missing_count = 0

        for num in arr:
            while current_num < num:
                missing_count += 1

                if missing_count == k:
                    return current_num
                
                current_num += 1
            current_num += 1

        
        while missing_count < k:
            missing_count += 1
            if missing_count == k:
                return current_num
            current_num += 1
        
        
                
                
        