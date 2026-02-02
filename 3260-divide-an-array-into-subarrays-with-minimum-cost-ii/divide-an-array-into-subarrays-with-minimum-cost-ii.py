from sortedcontainers import SortedList
from typing import List
import sys
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        k -= 1
        n = len(nums)
        ans = sys.maxsize
        left = SortedList()
        right = SortedList()
        summ = nums[0]

        for i in range(1, dist + 2):
            summ += nums[i]
            left.add(nums[i])
        
        def l2r():
            nonlocal summ
            x = left.pop()
            summ -= x
            right.add(x)
    
        def r2l():
            nonlocal summ
            x = right.pop(0)
            summ += x
            left.add(x)
        
        while len(left) > k:
            l2r()

        ans = summ

        for i in range(dist + 2, n):
            x = nums[i - dist - 1]
            if x in left:
                left.remove(x)
                summ -= x
            else:
                right.remove(x)
            
            y = nums[i]
            if not left or y < left[-1]:
                left.add(y)
                summ += y
            else:
                right.add(y)

            while len(left) < k and right:
                r2l()
            while len(left) > k:
                l2r()
            ans = min(ans, summ)
        return ans