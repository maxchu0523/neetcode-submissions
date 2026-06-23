class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        q = []
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append([r,c])

        dist = 0
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        while q:
            length = len(q)
            dist += 1
            for _ in range(0, length):
                row, col = q.pop(0)
                for dx, dy in direction:
                    shiftedX = row + dx
                    shiftedY = col + dy
                    if shiftedX >= 0 and shiftedY >= 0 and shiftedX < m and shiftedY < n :
                        if grid[shiftedX][shiftedY] == 2147483647:
                            grid[shiftedX][shiftedY] = dist
                            q.append([shiftedX,shiftedY])
        


            