class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        checked = [[0 for _ in range(m)] for _ in range(n)]
        moves = [0,1,2,3]
        i = 0
        j = 0
        move = (0,1) 
        ans = set()
        ans2= [matrix[0][0]]
        while len(ans2) != n*m:
            checked[i][j] = 1
            new_x = i + move[0]
            new_y = j + move[1]
            if 0 <= new_x < n and 0 <= new_y < m and checked[new_x][new_y] == 0:
                i = new_x
                j = new_y
                ans2.append(matrix[i][j])
                continue 
            else:
                if move == (0,1): move = (1,0)
                elif move == (1,0): move = (0,-1)
                elif move == (0,-1): move = (-1,0)
                else: move = (0,1)
        
        return ans2
            