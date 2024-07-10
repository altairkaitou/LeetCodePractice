class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = 0
        total = []
        weakest_row = []
        
        for index, soldier in enumerate(mat):
            soldiers = sum(soldier)
            total.append((soldiers, index))
        
        total.sort()

        for i in range(k):
            weakest_row.append(total[i][1])
        
        return weakest_row
            



      
        