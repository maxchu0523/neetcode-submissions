class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))
        

            def find(self, curr):
                if self.parent[curr] == curr:
                    return curr
                return self.find(self.parent[curr])

            def unite(self, u, v):
                uParrent = self.find(u)
                vParrent = self.find(v)
                if uParrent == vParrent:
                    return False
                self.parent[uParrent] = vParrent
                return True
            
        uf = UnionFind(n)
        res = n
        for u, v in edges:
            if uf.unite(u, v):
                res -= 1

        print(uf.parent)
        return res


        # graph = defaultdict(list)
        # for u, v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)
        # visited = set()

        # def dfs(i):
        #     for nei in graph[i]:
        #         if nei not in visited:
        #             visited.add(nei)
        #             dfs(nei)
        # res = 0
        # for i in range(n):
        #     if i not in visited:
        #         res += 1
        #         dfs(i)
        # return res