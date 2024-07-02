class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n + 1)]
        self.rank  = [1] * (n + 1)



    def find(self, u): 
        while u != self.parent[u]:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u 
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return 0
        if self.rank[pu] > self.rank[pv]:
            self.rank[pu] += self.rank[pv]
            self.parent[pv] = pu
        else:
            self.rank[pv] += self.rank[pu]
            self.parent[pu] = pv
            
        self.n -= 1
        return 1

    def isConnect(self):
        return self.n == 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice_uf = UnionFind(n)
        bob_uf = UnionFind(n)

        count = 0

        for typ, begin, end in edges:
            if typ == 3:
                count += (alice_uf.union(begin, end) | bob_uf.union(begin, end))

        for typ, begin, end in edges:
            if typ == 1:
                count += alice_uf.union(begin, end)
            elif typ == 2:
                count += bob_uf.union(begin, end)

        if bob_uf.isConnect() and alice_uf.isConnect():
            return len(edges) - count
        
        return -1



        


        
        