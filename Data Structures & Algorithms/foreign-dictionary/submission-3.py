import string
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        print(words)
        graph = defaultdict(list)
        indegree = defaultdict(int)
        alphabet = set()

        for word in words:
            for c in word:
                alphabet.add(c)
        for idx in range(1, len(words)):
            prev = words[idx-1]
            curr = words[idx]
            common = min(len(prev), len(curr))
            for x in range(common):
                if prev[x] != curr[x]:
                    graph[prev[x]].append(curr[x])
                    indegree[curr[x]] += 1
                    break
                else:  # for-else: runs if loop didn't break (no difference found)
                    if len(prev) > len(curr):
                        return ""

        print(graph)
        print(indegree)
        print(alphabet)

        q = deque([letter for letter in list(alphabet) if letter not in indegree ])
        order = ""
        print(q)
        while q:
            node = q.popleft()
            order += node
            for adj in graph[node]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)
        print(order)
        if len(alphabet) != len(order):
            return ""
        return order