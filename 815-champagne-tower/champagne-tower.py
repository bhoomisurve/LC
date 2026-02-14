class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * (i+1) for i in range(query_row+1)]
        dp[0][0] = poured
        
        for i in range(query_row):
            for j in range(i+1):
                excess = dp[i][j] - 1 if dp[i][j] > 1 else 0
                if excess > 0:
                    dp[i+1][j+1] += excess / 2
                    dp[i+1][j] += excess / 2
                    
        return min(dp[query_row][query_glass], 1)