class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x,y):
            visited[x][y] = 1 
            area=1 
            for move in moves: 
                new_x = x+move[0]
                new_y = y+move[1]
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                    if visited[new_x][new_y] == 0 and grid[new_x][new_y] == 1:
                        area += dfs(new_x,new_y)
            return area
        ans = 0
        moves = [(0,-1),(0,1),(1,0),(-1,0)]
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        counter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    area = dfs(i,j)
                    ans = max(ans,area)
       
        #print(visited)
        return ans 

