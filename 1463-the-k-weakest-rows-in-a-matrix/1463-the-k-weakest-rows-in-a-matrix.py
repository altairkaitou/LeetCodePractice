class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        soldier_count = []
        count = 0
        weakest_row = []

        for index, soldier in enumerate(mat):
            count = sum(soldier)

            soldier_count.append((count, index))

        soldier_count.sort()
        
        for i in range(k):
            weakest_row.append(soldier_count[i][1])

        
        return weakest_row
        