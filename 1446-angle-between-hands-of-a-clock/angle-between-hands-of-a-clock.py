class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12
        ha = hour * 30 + minutes * 0.5
        ma = minutes * 6
        d = abs(ha - ma)
        return min(d, 360 - d)