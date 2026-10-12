class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                moves = [(-1,0),(0,-1)]
                for move in moves:
                    new_x = i + move[0]
                    new_y = j + move[1]
                    if 0 <= new_x < m and 0 <= new_y < n:
                        dp[i][j] += dp[new_x][new_y]

        return dp[m-1][n-1]
