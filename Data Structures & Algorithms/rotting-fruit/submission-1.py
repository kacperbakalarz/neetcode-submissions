class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        counter = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                if grid[i][j] == 1:
                    counter += 1
        
        moves = [(0,-1),(0,1),(1,0),(-1,0)]
        while q: 
            x,y,days = q.popleft()
            if grid[x][y] == 1:
                grid[x][y] = 2
                counter -= 1
                if counter == 0:
                    return days
                
            for move in moves:
                new_x = x + move[0]
                new_y = y + move[1]
                if 0 <= new_x < n and 0 <= new_y < m:
                    if grid[new_x][new_y] == 1:
                        q.append((new_x,new_y,days+1))
        if counter == 0:
            return 0

        return -1
                


