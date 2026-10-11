class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i,j,0))

        moves = [(0,-1),(0,1),(1,0),(-1,0)]  
        while q:
            x,y,cost = q.popleft()
            #grid[x][y] = cost 
            for move in moves:
                new_x = x+move[0]
                new_y = y+move[1]
                new_cost = cost + 1
                if 0 <= new_x < n and 0 <= new_y < m:
                    if grid[new_x][new_y] == 2147483647:
                        grid[new_x][new_y] = new_cost
                        q.append((new_x,new_y,new_cost))

        
        