class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes = [[] for _ in range(n)]
        
        for e in edges:
            nodes[e[0]].append(e[1])
            nodes[e[1]].append(e[0])

        print(nodes)
        visited = set()
        res = True
        def dfs(p, i):
            nonlocal res
            if i in visited:
                res = False
            visited.add(i)
            if res:
                for n in nodes[i]:
                    if n != p:
                        dfs(i, n)
                        # if not res:
                        #     return False
        dfs(-1, 0)
        if len(visited) < n:
            return False
        return res

        