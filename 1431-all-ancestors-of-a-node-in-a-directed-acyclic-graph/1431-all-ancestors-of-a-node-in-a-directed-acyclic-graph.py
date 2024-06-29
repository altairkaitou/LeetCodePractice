class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)

        for from_node, to_node in edges:
            graph[to_node].append(from_node)

        def dfs(i):
            for y in graph[i]:
                if y not in visited:
                    visited.add(y)
                    dfs(y)
        
        d = defaultdict(list)

        for i in range(n):
            visited = set()
            dfs(i)
            d[i] = sorted(list(visited))
        return list(d.values())

        

        
