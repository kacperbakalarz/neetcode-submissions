class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #visited n x m
        #odplasz dfs, 
        """dfs(4) -> [1,1,1,1,3
                      1,0,0,0,2
                      3,2,2,2,2]
            dfs(2) -> -==-

            dfs(7) -> []"""
        n = len(heights)
        m = len(heights[0])
        visited_pacific = [[0 for _ in range(m)] for _ in range(n)]
        visited_atlantic = [[0 for _ in range(m)] for _ in range(n)]

        hash_pacific = []
        hash_atlantic = []

        for i in range(m):
            hash_pacific.append((0,i))
            hash_atlantic.append((n-1,i))

        for i in range(n):
            
            hash_pacific.append((i,0))
            hash_atlantic.append((i,m-1))
        
        hash_pacific = list(set(hash_pacific))
        hash_atlantic = list(set(hash_atlantic))
        print(hash_pacific)
        print(hash_atlantic)
        moves = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(x,y,visited):
            visited[x][y] = 1
            for move in moves:
                new_x = x + move[0]
                new_y = y + move[1]
                if 0 <= new_x < n and 0 <= new_y < m:
                    if visited[new_x][new_y] == 0 and heights[new_x][new_y] >= heights[x][y]:
                        dfs(new_x,new_y,visited)
        
        for start in hash_pacific:
            dfs(start[0],start[1],visited_pacific)
        
        for start in hash_atlantic:
            dfs(start[0],start[1],visited_atlantic)
        
        #print(visited_pacific)
        #print(visited_atlantic)
        ans = []
        for i in range(n):
            for j in range(m):
                if visited_pacific[i][j] == 1 and visited_atlantic[i][j] == 1:
                    ans.append((i,j))
        
        return ans 
        


        

            



        
    
        
        
            
        
