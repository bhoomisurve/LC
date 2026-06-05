class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minpr = float('inf')
        pr = 0
        for p in prices:
            minpr = min(minpr, p)
            pr = max(pr, p - minpr)
        return pr