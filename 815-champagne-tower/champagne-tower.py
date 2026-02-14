class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tow = [[0] * 102 for _ in range(102)]
        tow[0][0] = poured
        
        for r in range(query_row + 1):
            for c in range(r + 1):
                if tow[r][c] > 1:
                    excess = (tow[r][c] - 1.0) / 2.0
                    tow[r][c] = 1
                    tow[r+1][c] += excess
                    tow[r+1][c+1] += excess
                    
        return tow[query_row][query_glass]