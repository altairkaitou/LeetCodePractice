class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldier_count = []

        for i, soldier in enumerate(mat):
            count = sum(soldier)

            soldier_count.append((soldier, i))

        soldier_count.sort()

        weakest_row = []

        for i in range(k):
            weakest_row.append(soldier_count[i][1])

        return weakest_row




        