class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()

        def dfs(i):
            for nei in graph[i]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res