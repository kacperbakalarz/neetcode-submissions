class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0 for _ in range(m)] for _ in range(n)]

        if text1[0] == text2[0]: 
            dp[0][0] = 1
        else:
            dp[0][0] = 0
        


        for i in range(n):
            for j in range(m):

                if i == 0 and j == 0:
                    continue
                if j > 0:
                    up = dp[i][j-1]
                else:
                    up = -float('inf')
                if i > 0:
                    left = dp[i-1][j]
                else:
                    left = -float('inf')     

                if text1[i] == text2[j]:
                    if i - 1 >= 0 and j - 1 >= 0:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = 1
                else:
                    dp[i][j] = max(left,up)
        #print(dp)
        maxi = 0 
        for i in range(n):
            for j in range(m):
                maxi = max(maxi,dp[i][j])
        return maxi